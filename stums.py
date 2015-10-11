import requests
import bs4
import common
import authbase


class StudentManageSystem(authbase.AuthBase):
    def __init__(self, session_worker):
        super(StudentManageSystem, self).__init__(session_worker)
        self.session_worker = session_worker

        config = common.get_config()
        self.auth_url = config['url']['stums_auth']

    def access(self):
        return self.session_worker.get(self.auth_url)

    def get_grade(self):
        pass

    def get_syllabus(self):
        pass





