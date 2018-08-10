import asyncio
import paramiko
import logging
import traceback

logging.config.fileConfig('config/logging.conf')
logger = logging.getLogger('agoda')

class SftpDownloader:

    def __init__(self, site_cofig, file_name):
        self.site_config = site_cofig
        self.file_name = file_name

    def grabFile(self, host_name, user_name, password, remote_filename, local_filename):
        try:
            transport = paramiko.Transport(host_name, 22)
            transport.connect(username=user_name, password=password)
            sftp = paramiko.SFTPClient.from_transport(transport)
            sftp.get(remote_filename, local_filename)
            sftp.close()
            transport.close()
        except Exception:
            logger.error(traceback.format_exc())




    @asyncio.coroutine
    def download_and_save(self):
        self.grabFile(self.site_config.host_name, self.site_config.user_name,
                      self.site_config.password, self.file_name,
                      self.file_name)


