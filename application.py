import logging.config
from config.site_config import SiteConfig
from downloaders.downloader_factory import get_downloader
import asyncio
from urllib.parse import urlparse
import os

logging.config.fileConfig('config/logging.conf')
logger = logging.getLogger('agoda')


def extract_site_details_from_line(line):
    line = line.strip()
    details_array = line.split(',')
    dictionary = dict()
    parsed_url = urlparse(details_array[0])

    dictionary['url'] = details_array[0]
    dictionary['protocol'] = parsed_url.scheme
    dictionary['host_name'] = parsed_url.netloc
    dictionary['path'] = parsed_url.path
    if len(details_array) == 3:
        dictionary['user_name'] = details_array[1]
        dictionary['password'] = details_array[2]
    return dictionary


def get_site_configs():
    lines = None
    try:
        f = open('site_details', 'r')
        lines = f.readlines()
        f.close()
    except OSError:
        logger.error('Exiting application, site_details file not found')
        exit()
    result = []
    if lines:
        for line in lines:
            extracted_data = extract_site_details_from_line(line)
            result.append(SiteConfig(extracted_data.get('protocol'),
                                     extracted_data.get('url'),
                                     extracted_data.get('host_name', None),
                                     extracted_data.get('user_name', None),
                                     extracted_data.get('password', None)))
    return result


def extract_file_name(url):
    if url:
        splited_urls = url.split('/')
        for word in splited_urls[::-1]:
            if len(word) > 0:
                return word


if __name__ == '__main__':
    site_configs = get_site_configs()
    methods = []
    print('Enter output directory')
    path = input()

    if path and not os.path.exists(path):
        os.makedirs(path)
        if path[len(path)-1] != '/':
            path += '/'
    if not path:
        path = ''

    for site_config in site_configs:
        methods.append(get_downloader(site_config.protocol)(site_config,
                                                            extract_file_name(site_config.url), path).download_and_save())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(methods))




