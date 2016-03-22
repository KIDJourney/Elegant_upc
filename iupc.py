import requests
import hashlib
import common


class Iupc():
    def __init__(self):
        self.session = requests.Session()
        self.url_login, self.url_index = common.read_config_url()
        self.username, self.password = common.read_config_user()

        self.password = hashlib.md5(self.password.encode()).hexdigest()

    def is_available(self):
        response = self.get_content(self.url_index)
        return response
        # return response.status_code == 200
        # return 'CAS认证转向' in response.text

    def get_token(self):
        soup = self.get_content(self.url_login)
        token = soup.find('input', {'name': 'lt'}).get('value')
        return token

    def login(self):
        data = {'username': self.username,
                'password': self.password, 'lt': self.get_token(),
                "loginErrCnt": "0"
                }
        response = self.session.post(
            self.url_login, data=data, allow_redirects=False)

        if "错误的用户名或密码" in response.text:
            raise Exception("Username or password incorrect")

        access_response = self.get_content(self.url_index)

        access_url = access_response.find('a').get('href')

        response = self.session.get(access_url, allow_redirects=False)

        return response.status_code == 200

        # return "错误" not in response.text

    @common.bs4_decorator
    def get_content(self, *args, **kwargs):
        return self.session.get(*args, **kwargs)

if __name__ == "__main__":
    job = Iupc()
    response = job.login()
