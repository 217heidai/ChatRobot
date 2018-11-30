#!/usr/bin/python
# -*- encoding=utf-8 -*- s
# 文件名：tuling.py

import requests
import json

from uuid import getnode as get_mac

from location import Location

"""
图灵机器人
"""
class TulingRobot(object):
    def __init__(self):
        self.__apiKey = self.__get_apikey()
        self.__userId = self.__get_userId()
        self.__province, self.__city= self.__get_Location()

    def __get_apikey(self):# apiKey,机器人标识
        return 'apikey'
    
    def __get_userId(self):# userId,用户唯一标识
        return str(get_mac())[:32]
    
    def __get_Location(self):# 获取地理位置
        try:
            location = Location()
            country, province, city = location.get_Location()
            return province, city
        except:
            return '',''

    def __format_msg(self, msg):
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

    def chat(self, msg):
        try:
            url = 'http://openapi.tuling123.com/openapi/api/v2'
            body = self.__format_msg(msg)
            r = requests.post(url, data=body)
            respond = json.loads(r.text)
            mesageType = respond['results'][0]['resultType']
            if cmp(mesageType, 'text') == 0:
                mesage = respond['results'][0]['values']['text']
            else:
                mesage = u'抱歉, 我的大脑短路了,请稍后再试试...'
            return mesage
        except Exception:
            return u'抱歉, 我的大脑短路了,请稍后再试试...'
