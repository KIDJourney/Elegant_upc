#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-05-29 11:23:13
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-06-16 12:28:07

import requests
import bs4

class elegantupc :
    def __init__(self):
        self.url_index = "http://cas.upc.edu.cn/cas/login?service=http://i.upc.edu.cn/dcp/index.jsp"
        self.url_login = "http://cas.upc.edu.cn/cas/login"
        self.user_username = "1307010412"
        self.user_password = "Andthejourney123"
        self.user_token = ""
        self.user_request = None
        self.user_index = None

    def get_token(self):
        try :
            response = requests.get(self.url_index , timeout = 2)
        except requests.exceptions.Timeout :
            print("Connection time out , plz try again later")
            return

        soup = bs4.BeautifulSoup(response.text)
        try :
            result = soup.find_all(attrs={'name':'lt'})
            token = result[0].get('value')
        except :
            print("Get token error , plz contact with writer")
            return

        self.user_token = token

    def user_login(self):
        payload = {
            "encodedService":"http%3a%2f%2fi.upc.edu.cn%2fdcp%2findex.jsp",
            "service":"http://i.upc.edu.cn/dcp/index.jsp",
            "serviceName":"null",
            "username":self.user_username,
            "password":self.user_password,
            "lt":self.user_token,
            'autoLogin':"true"
        }
        self.user_request = requests.Session()
        response = self.user_request.post(self.url_login,data=payload)
        soup = bs4.BeautifulSoup(response.text)
        redireturl = soup.find('a').get('href')
        print(redireturl)




if __name__ == "__main__":
    job = elegantupc()
    job.get_token()
    job.user_login()
