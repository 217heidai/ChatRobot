#!/usr/bin/python
# -*- encoding=utf-8 -*- s
# 文件名：tuling.py

import json

import requests

from location import Location
from tools import Tools, switch


"""
图灵机器人
"""
class TulingRobot(object):
    def __init__(self):
        self.__tools = Tools()
        self.__apiKey = self.__get_apikey() # apiKey,机器人标识
        self.__userId = self.__get_userId() # userId,用户唯一标识
        self.__province, self.__city = self.__get_Location() # 通过IP定位，获取地理位置

    def __get_apikey(self):  # apiKey,机器人标识
        return 'a323758630ff4d6dacf72d90b316fc3c'

    def __get_userId(self):  # userId,用户唯一标识
        return self.__tools.get_cuid()

    def __get_Location(self):  # 获取地理位置
        try:
            location = Location()
            country, province, city = location.get_Location()
            return province, city
        except:
            return '', ''

    def __format_request(self, msg):
        msg = ''.join(msg)
        if len(self.__city) > 0:
            body = {
                "reqType": 0,
                "perception": {
                    "inputText": {
                        "text": msg
                    },
                    "selfInfo": {
                        "location": {
                            "city": self.__city,
                            "province": self.__province
                        }
                    }
                },
                "userInfo": {
                    "apiKey": self.__apiKey,
                    "userId": self.__userId
                }
            }
        else:
            body = {
                "reqType": 0,
                "perception": {
                    "inputText": {
                        "text": msg
                    }
                },
                "userInfo": {
                    "apiKey": self.__apiKey,
                    "userId": self.__userId
                }
            }
        return json.dumps(body)

    def __format_respond(self, respond):
        def format_text(values):
            return values['text'] + '\n'
        def format_url(values):
            return values['url'] + '\n'
        def format_news(values):
            msg = ''
            i = 1
            for news in values['news']:
                if len(news['name']) > 0:
                    #msg += i + u'、' +  news['info'] + ':\n' + news['name'] + '[' + news['detailurl'] + ']\n'
                    msg += str(i) + '.' + news['name'] + '\n'
                    i += 1
            return msg
        
        msg = ''
        for results in respond:
            resultType = results['resultType']
            values = results['values']
            for case in switch(resultType):
                if case('text'):
                    msg += format_text(values)
                    break
                if case('url'):
                    msg += format_url(values)
                    break
                if case('news'):
                    msg += format_news(values)
                    break
                if case('voice'):
                    pass
                if case('video'):
                    pass
                if case('image'):
                    pass
                if case():
                    msg = u'抱歉, 我的大脑短路了,请稍后再试试...'
        return msg


    def chat(self, msg):
        try:
            url = 'http://openapi.tuling123.com/openapi/api/v2'
            body = self.__format_request(msg)
            r = requests.post(url, data=body)
            respond = json.loads(r.text)
            #print respond
            return self.__format_respond(respond['results'])
        except Exception:
            return u'抱歉, 我的大脑短路了,请稍后再试试...'
