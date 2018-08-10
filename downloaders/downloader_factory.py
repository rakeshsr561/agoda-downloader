from enums.protocols import Protocol
from downloaders.ftp_downloader import FtpDownloader
from downloaders.http_downloader import HttpDownloader
from downloaders.https_downloader import HttpsDownloader
from downloaders.sftp_downloader import SftpDownloader
import logging.config

switcher = {
        Protocol.FTP.name: FtpDownloader,
        Protocol.HTTP.name: HttpDownloader,
        Protocol.SFTP.name: SftpDownloader,
        Protocol.HTTPS.name: HttpsDownloader
    }

logging.config.fileConfig('config/logging.conf')
logger = logging.getLogger('agoda')


def get_downloader(protocol):
    downloader = switcher.get(protocol.upper(), None)
    if not downloader:
        logger.error('Invalid protocol {}'.format(protocol))
    else:
        return downloader



