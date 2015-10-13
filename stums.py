import requests
import bs4
import common
import authbase
import re

class StudentManageSystem(authbase.AuthBase):
    def __init__(self, session_worker):
        super(StudentManageSystem, self).__init__(session_worker)
        self.session_worker = session_worker

        config = common.get_config()
        self.auth_url = config['url']['stums_auth']
        self.grade_url = config['stums']['grade']
        self.jwxt_cookie = {}

    def access(self):
        response = self.session_worker.get(self.auth_url)
        self.jwxt_cookie['JSESSIONID'] = re.findall('"[A-Z0-9a-z]+"', response.text)
        print(self.jwxt_cookie)
        return response

    def get_grade(self, page=1):
        request_payload = common.grade_check_payload_factor(page)
        response = self.session_worker.post(self.grade_url, data=request_payload)
        return response

    def get_syllabus(self):
        pass
