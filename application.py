import argparse
import logging.config
from utils.generic_utils import is_valid_url


logging.config.fileConfig('config/logging.conf')
logger = logging.getLogger('agoda')


def extract_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ftp_user')
    parser.add_argument('--ftp_password')
    parser.add_argument('--sftp_user')
    parser.add_argument('--sftp_password')
    parser.add_argument('--output_directory')
    return vars(parser.parse_args())


def get_urls_list():
    try:
        result = []
        f = open('urls', 'r')
        url_list = f.readlines()
        f.close()
        if not url_list:
            logger.info('Exiting application, There are no urls present in the file')
            exit()
        for url in url_list:
            if is_valid_url(url):
                result.append(url)
            else:
                logger.warning('Invalid url {}'.format(url))
        return result
    except OSError:
        logger.error('Exiting application, urls file not found')
        exit()




if __name__ == '__main__':
    arguments = extract_arguments()
    get_urls_list()
