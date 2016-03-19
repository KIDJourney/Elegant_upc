import configparser

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

    return username , password

if __name__ == "__main__":
    print(read_config_url_login())
    print(read_config_user())