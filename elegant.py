#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kidjourney
# @Date:   2015-05-29 11:23:13
# @Last Modified by:   kidjourney
# @Last Modified time: 2015-06-17 09:18:29

import requests
import bs4
import configparser

class elegantupc :
    def __init__(self):
        self.url_index = "http://cas.upc.edu.cn/cas/login?service=http://i.upc.edu.cn/dcp/index.jsp"
        self.url_login = "http://cas.upc.edu.cn/cas/login"
        self.url_userpage = "http://i.upc.edu.cn/dcp/forward.action?path=/portal/portal&p=wkHomePage"
        self.user_username = ""
        self.user_password = ""
        self.user_token = ""
        self.user_request = None #container of status of connection

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
        # getSession
        self.user_request.get(redireturl)

        response = self.user_request.get(self.url_userpage) #Login to index of digital upc
        # get Session already
        # print(response.text)

    def jwxt_login(self):
        pass

    def library_login(self):
        response = self.user_request.get('http://i.upc.edu.cn/dcp/forward.action?path=dcp/apps/sso/jsp/ssoDcpSelf&appid=1186')
        #Get Session

    def card_login(self):
        response = self.user_request.get('http://card.upc.edu.cn/Login.aspx')
        soup = bs4.BeautifulSoup(response.text)
        redirecturl = soup.find('a').get('href')

if __name__ == "__main__":
    job = elegantupc()
    job.get_token()
    job.user_login()
    job.card_login()