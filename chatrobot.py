#!/usr/bin/python
# -*- encoding=utf-8 -*- s
# 文件名：chatrobot.py

import os

from baidustt import BaiduSTT
from baidutts import BaiduTTS
from tools import Tools
from tuling import TulingRobot
from voice import Voice


class ChatRobot(object):
    def __init__(self):
        self.__tools = Tools()
        self.__baiduSTT = BaiduSTT() # 语音转文字模块
        self.__baiduTTS = BaiduTTS() # 文字转语音模块
        self.__voice = Voice() # 音频抓取模块
        self.__tuling = TulingRobot() # 图灵机器人
        
    def textchat(self):
        print("Now u can type in something & input q to quit\n")
        while True:
            """"文字聊天"""
            request = raw_input("Master:")
            if request == 'q':
                exit("u r quit the chat !")         # 设定输入q，退出聊天。
            else:
                response = self.__tuling.chat(request)
                print "Robot:%s" % (response)
                speechFile = self.__baiduTTS.TTS(response)
                if os.path.exists(speechFile):
                    self.__tools.play_mp3(speechFile)
                    os.remove(speechFile)

    def voicechat(self): 
        print("Now u can talk to me\n")
        while True:
            """"语音聊天"""
            speechFile = self.__voice.get_voice()
            if os.path.exists(speechFile):
                request = self.__baiduSTT.STT(speechFile)
                print request
                response = self.__tuling.chat(request)
                print response
                speechFile = self.__baiduTTS.TTS(response)
                if os.path.exists(speechFile):
                    self.__tools.play_mp3(speechFile)
                    os.remove(speechFile)


if __name__ == '__main__':
    chatRobot = ChatRobot()
    chatRobot.textchat()
    #chatRobot.voicechat()
