import asyncio
from ftplib import FTP
import traceback


class FtpDownloader:

    def __init__(self, site_cofig, file_name):
        self.site_config = site_cofig
        self.file_name = file_name

    def grabFile(self, host_name, user_name, password, guest_file_name, host_file_name):
        ftp = FTP(host_name)
        ftp.login(user_name, password)
        localfile = open(host_file_name, 'wb')
        ftp.retrbinary('RETR ' + guest_file_name, localfile.write, 1024)
        ftp.quit()
        localfile.close()

    @asyncio.coroutine
    def download_and_save(self):
        try:

            self.grabFile(self.site_config.host_name, self.site_config.user_name,
                          self.site_config.password, self.file_name,
                          self.file_name)

        except Exception as e:
            print(traceback.format_exc())


