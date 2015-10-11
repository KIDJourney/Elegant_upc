import requests
import bs4
import common
import authbase


class StudentManageSystem(authbase.AuthBase):
    def __init__(self, session_worker):
        super(StudentManageSystem, self).__init__(session_worker)
        self.session_worker = session_worker

        self

