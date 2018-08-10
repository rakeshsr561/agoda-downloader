class SiteConfig:
    def __init__(self, protocol, url, host_name, user_name=None, password=None):
        self.url = url
        self.host_name = host_name
        self.protocol = protocol
        self.user_name = user_name
        self.password = password


