import requests
import bs4
import common

class Library:
    def __init__(self, session_worker):

        if not isinstance(session_worker, requests.Session):
            raise Exception("Type Error : Session worker must be instance of requests.Session")
        if not common.login_check(session_worker):
            raise Exception("Login Error : Login error or not logged session")

        self.session_worker = session_worker
        self.config = common.get_config()
        self.library_redirect = self.config['url']['library_redirect']

    def access_session(self):
        resposne = self.session_worker.get(self.library_redirect)
        resposne.encoding = 'utf8'
        return resposne


    def get_books_borrowed(self):
        pass
