from unittest import TestCase
from downloaders.https_downloader import HttpsDownloader
from downloaders.http_downloader import HttpDownloader
from downloaders.ftp_downloader import FtpDownloader
from downloaders.sftp_downloader import SftpDownloader
from downloaders.downloader_factory import get_downloader
import unittest
from config.site_config import SiteConfig


class MyTest(TestCase):

    def test_downloader_factory(self):
        self.assertIsInstance(HttpsDownloader(SiteConfig('p','u','h'), 'file'), get_downloader('https'))
        self.assertIsInstance(HttpDownloader(SiteConfig('p', 'u', 'h'), 'file'), get_downloader('http'))
        self.assertIsInstance(FtpDownloader(SiteConfig('p', 'u', 'h'), 'file'), get_downloader('ftp'))
        self.assertIsInstance(SftpDownloader(SiteConfig('p', 'u', 'h'), 'file'), get_downloader('sftp'))


if __name__ == '__main__':
    unittest.main()

