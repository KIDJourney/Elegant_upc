import requests
import common


class AuthBase:
    def __init__(self, session_worker):
        if not isinstance(session_worker, requests.Session):
            raise Exception("Type Error : Session worker must be instance of requests.Session")
        if not common.login_check(session_worker):
            raise Exception("Login Error : Login error or not logged session")


