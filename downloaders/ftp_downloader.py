import asyncio

import ftplib
import traceback
import logging.config
import os

logging.config.fileConfig('config/logging.conf')
logger = logging.getLogger('agoda')


class FtpDownloader:

    def __init__(self, site_cofig, file_name, path=''):
        self.site_config = site_cofig
        self.file_name = file_name
        self.path = path

    @asyncio.coroutine
    def download_and_save(self):
        try:
            ftp = ftplib.FTP(self.site_config.host_name)
            ftp.login(self.site_config.user_name, self.site_config.password)
            localfile = open(self.path + self.file_name, 'wb')
            ftp.retrbinary('RETR ' + self.file_name, localfile.write, 1024)
            ftp.quit()
            localfile.close()
        except Exception:
            logger.error("Exception while downloading from url {}".format(self.site_config.url))
            logger.error(traceback.format_exc())
            try:
                os.remove(self.path + self.file_name)
            except OSError:
                pass


