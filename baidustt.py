#!/usr/bin/python
# -*- encoding=utf-8 -*- s
# 文件名：baidustt.py

import os

from aip import AipSpeech

from tools import Tools

"""
语音转文字
"""
class BaiduSTT(object):
    def __init__(self):
        self.__tools = Tools()
        self.__AppID = self.__get_AppID() # 百度AppID
        self.__APIKey = self.__get_APIKey() # 百度APIKey
        self.__SecretKey = self.__get_SecretKey() # 百度SecretKey
        self.__format = self.__get_format() # 语音文件的格式，pcm 或者 wav 或者 amr。不区分大小写。推荐pcm文件
        self.__rate = self.__get_rate() # 采样率，16000，固定值
        self.__cuid = self.__get_cuid() # 用户唯一标识，用来区分用户，填写机器 MAC 地址或 IMEI 码，长度为60以内
        self.__dev_pid = self.__get_dev_pid() # 不填写lan参数生效，都不填写，默认1537（普通话 输入法模型）
        self.__client = AipSpeech(self.__AppID, self.__APIKey, self.__SecretKey)

    def __get_AppID(self): # 百度AppID
        return '14998128'
    
    def __get_APIKey(self): # 百度APIKey
        return 'maUfjhtuP3LBrfXmBsfyhtIF'
    
    def __get_SecretKey(self): # 百度SecretKey
        return '6xhMVKhpI7rSzHu7koO8H6GVr0y17wK5'

    def __get_format(self): # 语音文件的格式，pcm 或者 wav 或者 amr。不区分大小写。推荐pcm文件
        return 'pcm'

    def __get_rate(self): # 采样率，16000，固定值
        return '16000'

    def __get_cuid(self): # 用户唯一标识，用来区分用户，填写机器 MAC 地址或 IMEI 码，长度为60以内
        return self.__tools.get_cuid()
    
    """
    1536:普通话(支持简单的英文识别),搜索模型,无标点,支持自定义词库
    1537:普通话(纯中文识别),输入法模型,有标点,不支持自定义词库
    1737:英语,有标点,不支持自定义词库
    1637:粤语,有标点,不支持自定义词库
    1837:四川话,有标点,不支持自定义词库
    1936:普通话远场,远场模型,有标点,不支持
    """
    def __get_dev_pid(self): # 不填写lan参数生效，都不填写，默认1537（普通话 输入法模型）
        return '1537'

    def STT(self, speechFile): # 输入语音文件（mp3、wav、pcm格式），输出文字
        def get_file_content(filePath):
            with open(filePath, 'rb') as fp:
                return fp.read()
        
        if not os.path.exists(speechFile):
            return ''
        try:
            speechFile = self.__tools.format_audio(speechFile)
            result = self.__client.asr(get_file_content(speechFile), self.__format, self.__rate, {'cuid': self.__cuid,
                                                                                                  'dev_pid': self.__dev_pid})
            #print result
            return result['result'][0] # 提供1-5个候选结果，utf-8 编码
        except:
            return ''

if __name__ == '__main__':
    baiduSTT = BaiduSTT()
    print baiduSTT.STT('speech-original.mp3')