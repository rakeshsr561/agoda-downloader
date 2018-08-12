import asyncio
import paramiko
import logging.config
import traceback
import os

logging.config.fileConfig('config/logging.conf')
logger = logging.getLogger('agoda')


class SftpDownloader:

    def __init__(self, site_cofig, file_name, path=''):
        self.site_config = site_cofig
        self.file_name = file_name
        self.path = path


    @asyncio.coroutine
    def download_and_save(self):
        try:
            transport = paramiko.Transport(self.site_config.host_name, 22)
            transport.connect(username=self.site_config.user_name, password=self.site_config.password)
            sftp = paramiko.SFTPClient.from_transport(transport)
            sftp.get(self.file_name, self.path + self.file_name)
            sftp.close()
            transport.close()
        except Exception:
            logger.error("Exception while downloading from url {}".format(self.site_config.url))
            logger.error(traceback.format_exc())
            try:
                os.remove(self.path + self.file_name)
            except OSError:
                pass

