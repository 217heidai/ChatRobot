#!/usr/bin/python
# -*- encoding=utf-8 -*- s
# 文件名：voice.py


import speech_recognition as sr

class Voice(object):
    def __init__(self):
        self.__r = sr.Recognizer()
        self.__filename = "speech.wav"

    def get_voice(self):
        with sr.Microphone() as source: # use the default microphone as the audio source
            audio = self.__r.listen(source) # listen for the first phrase and extract it into audio data
        try:
            print self.__r.recognize_sphinx(audio)
            return self.__filename
        except:
            return ''
        
if __name__ == '__main__':
    voice = Voice()
    voice.get_voice()