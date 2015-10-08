import bs4
import requests
import configparser


class iupc:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.url_index = config['url']['index']
        self.url_login = config['url']['login']
        self.user_username = config['info']['username']
        self.user_password = config['info']['password']
        self.user_token = ""  # token get from login page
        self.request_session = requests.Session()  # container of status of connection
        self.app_page = "http://i.upc.edu.cn/dcp/forward.action?path=/portal/portal&p=home"
        self.login_status = False

    def get_token(self):
        try:
            login_soup = self.request_session.get(self.url_login)
            login_soup = bs4.BeautifulSoup(login_soup.text, 'lxml')

            token = login_soup.find('input', {'name': 'lt'})['value']
            self.user_token = token

        except Exception as inst:
            print(inst)
            print("Process terminate .")

    def login(self):
        payload = self.payload_factor()
        status_page = self.request_session.post(self.url_login, payload)

        if "错误" in status_page.text:
            print("Login failed , Check your username and password config")
            raise Exception("Login failed Error")

        rediect_url = bs4.BeautifulSoup(status_page.text, 'lxml').find('a')['href']

        self.request_session.get(rediect_url)

        login_check = self.request_session.get(self.app_page, allow_redirects=False)
        if login_check.status_code == 200:
            print("Login Success !")
            self.login_status = True
        else:
            print("Login Failed , please check your ")
            raise Exception("Login Error")

    def payload_factor(self):
        payload = {
            "encodedService": "http%3a%2f%2fi.upc.edu.cn%2fdcp%2findex.jsp",
            "service": "http://i.upc.edu.cn/dcp/index.jsp",
            "serviceName": "null",
            "loginErrCnt": '0',
            "username": self.user_username,
            "password": self.user_password,
            "lt": self.user_token,
            'autoLogin': "on"
        }
        return payload

    def access_url(self, url, method='get', payload=None):
        if not self.login_status:
            raise Exception("Login Status Error : You haven't logined in")

        active = {
            'get': self.request_session.get(url),
            'post': self.request_session.post(url, data=payload)
        }

        if method not in ('get','post') :
            raise Exception("Method Error : Method %s does not exist ")

        return bs4.BeautifulSoup(active[method.lower()].text, 'lxml')


if __name__ == "__main__":
    unit_tester = iupc()
    unit_tester.get_token()
    unit_tester.login()
    print(unit_tester.access_url(unit_tester.app_page).prettify())
