import bs4
import requests
import configparser
import library
import common
import stums

class ElegantUpc:
    def __init__(self):
        config = common.get_config()

        self.url_index = config['url']['index']
        self.url_app = config['url']['app']
        self.url_login = config['url']['login']
        self.user_username = config['info']['username']
        self.user_password = config['info']['password']

        self.user_token = ""  # token get from login page
        self.request_session = requests.Session()  # container of status of connection
        self.login_status = False

    def get_token(self):
        try:
            login_soup = self.request_session.get(self.url_login)
            login_soup = bs4.BeautifulSoup(login_soup.text)

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

        redirect_url = bs4.BeautifulSoup(status_page.text).find('a')['href']

        self.request_session.get(redirect_url)

        login_check = self.request_session.get(self.url_app, allow_redirects=False)
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


if __name__ == "__main__":
    unit_tester = ElegantUpc()
    unit_tester.get_token()
    unit_tester.login()
    stums_worker = stums.StudentManageSystem(unit_tester.request_session)
    common.access_url(stums_worker.session_worker,)
