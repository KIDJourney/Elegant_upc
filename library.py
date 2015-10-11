import requests
import bs4
import common
import authbase


class Library(authbase.AuthBase):
    def __init__(self, session_worker):
        super(Library,self).__init__(session_worker)

        self.config = common.get_config()
        self.library_redirect = self.config['url']['library_redirect']

    def access_session(self):
        response = self.session_worker.get(self.library_redirect)
        response.encoding = 'utf8'
        return response


    def get_books_borrowed(self):
        pass
