import requests
import configparser


def login_check(session_worker):
    if not isinstance(session_worker,requests.Session):
            raise Exception("Type Error , Session worker must be instance of requests.Session")
    config = configparser.ConfigParser()
    config.read('config.ini')

    response = session_worker.get(config['url']['app'], allow_redirects=False)
    return response.status_code == 200


def get_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

