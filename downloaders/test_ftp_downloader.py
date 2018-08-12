from unittest import TestCase
import asyncio
import unittest
from downloaders import ftp_downloader
from config.site_config import SiteConfig
from unittest.mock import patch


class MyTest(TestCase):

    def setUp(self):
        self.fd = ftp_downloader.FtpDownloader(SiteConfig('protocol', 'url', 'host_name', 'user_name', 'password'), 'file')

    def tearDown(self):
        import os
        os.remove("file")

    def test_download_file(self):
        with patch('downloaders.ftp_downloader.ftplib.FTP') as ftp_mock:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self.fd.download_and_save())
            ftp_mock.assert_called_with('host_name')
            mock_ftp = ftp_mock.return_value
            self.assertTrue(mock_ftp.login.called)
            mock_ftp.login.assert_called_with('user_name', 'password')
            self.assertTrue(mock_ftp.retrbinary.called)
            self.assertTrue(mock_ftp.quit.called)


if __name__ == '__main__':
    unittest.main()

