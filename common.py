import configparser
from bs4 import BeautifulSoup


def read_config_jwxt():
    config = configparser.ConfigParser()
    config.read('config.ini')

    jwxt_auth = config['url']['jwxt_auth']

    return jwxt_auth


def read_config_url():
    config = configparser.ConfigParser()
    config.read('config.ini')

    login = config['url']['login']
    index = config['url']['index']
    # username = config['user']['username']
    # password = config['user']['password']

    return login, index


def read_config_user():
    config = configparser.ConfigParser()
    config.read('config.ini')

    username = config['user']['username']
    password = config['user']['password']

    return username, password


def bs4_decorator(fuc):
    def soup_generator(self, *args, **kwargs):
        response = fuc(self, *args, **kwargs).text
        return BeautifulSoup(response, 'lxml')
    return soup_generator


if __name__ == "__main__":
    print(read_config_url_login())
    print(read_config_user())
