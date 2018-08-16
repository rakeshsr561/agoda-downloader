from unittest import TestCase
import asyncio
import unittest
from downloaders import https_downloader
from config.site_config import SiteConfig
from unittest.mock import patch
from unittest.mock import Mock


class TestHttpsDownloader(TestCase):

    def setUp(self):
        self.fd = https_downloader.HttpsDownloader(SiteConfig('protocol', 'url',
                                                            'host_name', 'user_name', 'password'), 'file')

    def tearDown(self):
        import os
        if os.path.exists("file"):
            os.remove("file")

    def test_download_file(self):
        with patch('downloaders.https_downloader.requests') as requests_mock:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self.fd.download_and_save())
            self.assertTrue(requests_mock.get.called)
            requests_mock.get.assert_called_with('https://host_name/file', stream=True)

    def test_delete_partial_download_file(self):
        with patch('downloaders.https_downloader.requests') as requests_mock:
            f = open('file', 'wb')
            f.close()
            loop = asyncio.get_event_loop()
            requests_mock.get.side_effect = Mock(side_effect=Exception())
            loop.run_until_complete(self.fd.download_and_save())
            import os.path
            self.assertFalse(os.path.exists('file'))


if __name__ == '__main__':
    unittest.main()

