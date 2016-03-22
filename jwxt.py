import requests
from bs4 import BeautifulSoup
import common


class Jwxt:
    def __init__(self, session):
        self.session = session
        self.jwxt_auth = common.read_config_jwxt()

    def __check_available(self):
        pass

    def auth(self):
        return self.get_response(self.jwxt_auth)

    def get_response(self, *args, **kwargs):
        return self.session.get(*args, **kwargs)
