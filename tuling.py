#!/usr/bin/python
# -*- encoding=utf-8 -*- s
# 文件名：tuling.py

import requests
import json
import logging

from uuid import getnode as get_mac


class TulingRobot():
    def __init__(self):
        self.__apiKey = self.__get_apikey()
        self.__userId = self.__get_userId()

    def __get_apikey(self):# apiKey,机器人标识
        return 'a323758630ff4d6dacf72d90b316fc3c'
    
    def __get_userId(self):# userId,用户唯一标识
        return str(get_mac())[:32]

    def __format_msg(self, msg):
        msg = ''.join(msg)
        body = {
            "reqType": 0,
            "perception": {
                "inputText": {
                    "text": msg
                },
                "selfInfo": {
                    "location": {
                        "city": "上海",
                        "province": "上海",
                        "street": "上海"
                    }
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


if __name__ == '__main__':
    Robot = TulingRobot()

    print("Now u can type in something & input q to quit")
    while True:
        msg = raw_input("\nMaster:")
        if msg == 'q':
            exit("u r quit the chat !")         # 设定输入q，退出聊天。
        else:
            turing_data = Robot.chat(msg)
            print "Robot:%s" % (turing_data)