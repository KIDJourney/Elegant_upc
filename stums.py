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

    def access(self):
        redirect_content = self.session_worker.get(self.auth_url ,allow_redirects = False).text

        jwxt_auth = re.findall('<a href="(.+)"',redirect_content)[0]

        self.session_worker = requests.Session()

        response = self.session_worker.get(jwxt_auth)

        return response.text

    def get_grade(self, page=1):
        request_payload = common.grade_check_payload_factor(page)
        response = self.session_worker.post(self.grade_url, data=request_payload)
        return response

    def get_syllabus(self):
        pass
