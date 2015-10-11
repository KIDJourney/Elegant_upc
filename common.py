import requests
import configparser
import bs4

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


def access_url(session_worker, url, method='get', payload=None):
    active = {
        'get': session_worker.get(url),
        'post': session_worker.post(url, data=payload)
    }

    if method not in ('get', 'post'):
        raise Exception("Method Error : Method %s does not exist ")

    return bs4.BeautifulSoup(active[method.lower()].text)

