import asyncio
import paramiko
import traceback


class SftpDownloader:

    def __init__(self, site_cofig, file_name):
        self.site_config = site_cofig
        self.file_name = file_name


    @asyncio.coroutine
    def download_and_save(self):
        try:
            transport = paramiko.Transport(self.site_config.host_name, 22)
            transport.connect(username=self.site_config.user_name, password=self.site_config.password)
            sftp = paramiko.SFTPClient.from_transport(transport)
            sftp.get(self.file_name, self.file_name)
            sftp.close()
            transport.close()
        except Exception:
            print(traceback.format_exc())
