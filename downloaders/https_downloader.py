import asyncio
import requests


class HttpsDownloader:

    def __init__(self, site_cofig, file_name):
        self.site_config = site_cofig
        self.file_name = file_name

    def grabFile(self, host_name, remote_filename, local_filename):
        r = requests.get('http://' + host_name + '/' + remote_filename, stream=True)
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

    @asyncio.coroutine
    def download_and_save(self):
        print('hi')
        self.grabFile(self.site_config.host_name,  self.file_name,
                      self.file_name)
