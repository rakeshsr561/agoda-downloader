import asyncio
import requests
import logging.config
import traceback
import os

logging.config.fileConfig('config/logging.conf')
logger = logging.getLogger('agoda')


class HttpsDownloader:

    def __init__(self, site_cofig, file_name, path=''):
        self.site_config = site_cofig
        self.file_name = file_name
        self.path = path

    @asyncio.coroutine
    def download_and_save(self):
        try:
            r = requests.get('https://' + self.site_config.host_name + '/' + self.file_name, stream=True)
            with open(self.path + self.file_name, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
        except Exception:
            logger.error("Exception while downloading from url {}".format(self.site_config.url))
            logger.error(traceback.format_exc())
            try:
                os.remove(self.path + self.file_name)
            except OSError:
                pass

