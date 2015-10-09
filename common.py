import requests
import configparser

def login_check(session_worker):
    if not isinstance(session_worker,requests.Session):
            raise Exception("Type Error , Session worker must be instance of requests.Session")
    config = configparser.ConfigParser()
    config.read('config.ini')

    login_check = session_worker.get(config['url']['app'], allow_redirects=False)
    return login_check.status_code == 200

def get_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config

