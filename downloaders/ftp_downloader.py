import asyncio

import ftplib
import traceback


class FtpDownloader:

    def __init__(self, site_cofig, file_name):
        self.site_config = site_cofig
        self.file_name = file_name

    @asyncio.coroutine
    def download_and_save(self):
        try:
            ftp = ftplib.FTP(self.site_config.host_name)
            ftp.login(self.site_config.user_name, self.site_config.password)
            localfile = open(self.file_name, 'wb')
            ftp.retrbinary('RETR ' + self.file_name, localfile.write, 1024)
            ftp.quit()
            localfile.close()
        except Exception:
            print(traceback.format_exc())


