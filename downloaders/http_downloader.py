import asyncio
import requests


class HttpDownloader:

    def __init__(self, site_cofig, file_name):
        self.site_config = site_cofig
        self.file_name = file_name

    @asyncio.coroutine
    def download_and_save(self):
        r = requests.get('http://' + self.site_config.host_name + '/' + self.file_name, stream=True)
        with open(self.file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
