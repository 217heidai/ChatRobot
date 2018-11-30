#!/usr/bin/python
# -*- encoding=utf-8 -*- s
# 文件名：chatrobot.py

from tuling import TulingRobot

class ChatRobot(object):
    def __init__(self):
        self.__tuling = TulingRobot()

    def chat(self):
        print("Now u can type in something & input q to quit")
        while True:
            msg = raw_input("\nMaster:")
            if msg == 'q':
                exit("u r quit the chat !")         # 设定输入q，退出聊天。
            else:
                request = self.__tuling.chat(msg)
                print "Robot:%s" % (request)

if __name__ == '__main__':
    chatRobot = ChatRobot()
    chatRobot.chat()