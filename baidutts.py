#!/usr/bin/python
# -*- encoding=utf-8 -*- s
# 文件名：baidutts.py

import os

from aip import AipSpeech

from tools import Tools


"""
文字转语音
"""
class BaiduTTS(object):
    def __init__(self):
        self.__tools = Tools()
        self.__AppID = self.__get_AppID() # 百度AppID
        self.__APIKey = self.__get_APIKey() # 百度APIKey
        self.__SecretKey = self.__get_SecretKey() # 百度SecretKey
        self.__lang = self.__get_lang() # 语言选择,填写zh
        self.__ctp = self.__get_ctp() # 客户端类型选择，web端填写1
        self.__cuid = self.__get_cuid() # 用户唯一标识，用来区分用户，填写机器 MAC 地址或 IMEI 码，长度为60以内
        self.__spd = self.__get_spd() # 语速，取值0-9，默认为5中语速
        self.__pit = self.__get_pit() # 音调，取值0-9，默认为5中语调
        self.__vol = self.__get_vol() # 音量，取值0-15，默认为5中音量
        self.__per = self.__get_per() # 发音人选择, 0为女声，1为男声，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女
        self.__client = AipSpeech(self.__AppID, self.__APIKey, self.__SecretKey)

    def __get_AppID(self): # 百度AppID
        return '14998128'
    
    def __get_APIKey(self): # 百度APIKey
        return 'maUfjhtuP3LBrfXmBsfyhtIF'
    
    def __get_SecretKey(self): # 百度SecretKey
        return '6xhMVKhpI7rSzHu7koO8H6GVr0y17wK5'

    def __get_lang(self): # 语言选择,填写zh
        return 'zh'

    def __get_ctp(self): # 客户端类型选择，web端填写1
        return '1'
    
    def __get_cuid(self): # 用户唯一标识，用来区分用户，填写机器 MAC 地址或 IMEI 码，长度为60以内
        return self.__tools.get_cuid()

    def __get_spd(self): # 语速，取值0-9，默认为5中语速
        return '5'
    
    def __get_pit(self): # 音调，取值0-9，默认为5中语调
        return '5'

    def __get_vol(self): # 音量，取值0-15，默认为5中音量
        return '5'

    def __get_per(self): # 发音人选择, 0为女声，1为男声，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女
        return '0'

    def TTS(self, msg):#输入文字，输出语音文件（MP3格式）
        speechFile = 'speech.mp3'
        if os.path.exists(speechFile):
            os.remove(speechFile)
        try:
            result = self.__client.synthesis(msg, self.__lang, self.__ctp, {'cuid': self.__cuid, 
                                                                            'spd': self.__spd, 
                                                                            'pit': self.__pit, 
                                                                            'vol': self.__vol, 
                                                                            'per': self.__per})
            if not isinstance(result, dict):
                with open(speechFile, 'wb') as f:
                    f.write(result)
                return speechFile
            else:
                return ''
        except:
            return ''


if __name__ == '__main__':
    baiduTTS = BaiduTTS()
    baiduTTS.TTS(u'你好，主人')
