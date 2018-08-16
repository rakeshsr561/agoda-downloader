from unittest import TestCase
import asyncio
import unittest
from downloaders import sftp_downloader
from config.site_config import SiteConfig
from unittest.mock import patch
from unittest.mock import Mock


class TestSftpDownloader(TestCase):

    def setUp(self):
        self.fd = sftp_downloader.SftpDownloader(SiteConfig('protocol', 'url',
                                                            'host_name', 'user_name', 'password'), 'file')

    def test_download_file(self):
        with patch('downloaders.sftp_downloader.paramiko') as paramiko_mock:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self.fd.download_and_save())
            paramiko_mock.Transport.assert_called_with('host_name', 22)
            transport_mock = paramiko_mock.Transport.return_value
            self.assertTrue(transport_mock.connect.called)
            sftp_client_mock = paramiko_mock.SFTPClient.from_transport.return_value
            self.assertTrue(sftp_client_mock.get.called)
            self.assertTrue(sftp_client_mock.close.called)
            sftp_client_mock.get.assert_called_with('file', 'file')
            self.assertTrue(transport_mock.close.called)

    def test_delete_partial_download_file(self):
        with patch('downloaders.sftp_downloader.paramiko') as paramiko_mock:
            f = open('file', 'wb')
            f.close()
            transport_mock = paramiko_mock.Transport.return_value
            transport_mock.close.side_effect = Mock(side_effect=Exception())
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self.fd.download_and_save())
            import os.path
            self.assertFalse(os.path.exists('file'))





if __name__ == '__main__':
    unittest.main()

