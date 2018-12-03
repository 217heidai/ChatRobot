#!/usr/bin/python
# -*- encoding=utf-8 -*- s
# 文件名：tools.py

import os
import platform
import re
import subprocess
import sys
import time
from uuid import getnode as get_mac


class Tools(object):
    def __init__(self):
        self.__platform = self.__get_platform()

    def validate_ipv4(self, ip_str):  # ipv4地址合法性判断
        sep = ip_str.split('.')
        if len(sep) != 4:
            return False
        for i, x in enumerate(sep):
            try:
                int_x = int(x)
                if int_x < 0 or int_x > 255:
                    return False
            except:
                return False
        return True

    def validate_ipv6(self, ip_str):  # ipv6地址合法性判断
        #:Regex for validating an IPv6 in hex notation
        _HEX_RE = re.compile(
            r'^:{0,1}([0-9a-fA-F]{0,4}:){0,7}[0-9a-fA-F]{0,4}:{0,1}$')

        #:Regex for validating an IPv6 in dotted-quad notation
        _DOTTED_QUAD_RE = re.compile(
            r'^:{0,1}([0-9a-fA-F]{0,4}:){2,6}(\d{1,3}\.){3}\d{1,3}$')
        if _HEX_RE.match(ip_str):
            if ':::' in ip_str:
                return False
            if '::' not in ip_str:
                halves = ip_str.split(':')
                return len(halves) == 8 and halves[0] != '' and halves[-1] != ''
            halves = ip_str.split('::')
            if len(halves) != 2:
                return False
            if halves[0] != '' and halves[0][0] == ':':
                return False
            if halves[-1] != '' and halves[-1][-1] == ':':
                return False
            return True

        if _DOTTED_QUAD_RE.match(ip_str):
            if ':::' in ip_str:
                return False
            if '::' not in ip_str:
                halves = ip_str.split(':')
                return len(halves) == 7 and halves[0] != ''
            halves = ip_str.split('::')
            if len(halves) > 2:
                return False
            hextets = ip_str.split(':')
            quads = hextets[-1].split('.')
            for q in quads:
                if int(q) > 255 or int(q) < 0:
                    return False
            return True
        return False

    def __get_platform(self):
        sysstr = platform.system()
        if(sysstr == 'Windows'):
            return 'Windows'
        elif(sysstr == 'Linux'):
            return 'Linux'
        else:
            return 'MAC'

    def play_mp3(self, MP3file):
        if self.__platform == 'MAC':
            subprocess.call(['afplay', MP3file])
        elif self.__platform == 'Linux':
            subprocess.call(['mplayer', MP3file])
        else:
            pass

    def get_cuid(self): # 获取本机MAC地址
        return str(get_mac())[:32]

    def format_audio(self, audiofile): #音频格式转换
        if not os.path.exists(audiofile):
            return ''
        speechFile = 'speech.pcm'
        filetype = audiofile[-3:]
        if (cmp(filetype, 'mp3') == 0) or (cmp(filetype, 'wav') == 0):
            cmd = 'ffmpeg -y  -i %s  -acodec pcm_s16le -f s16le -ac 1 -ar 16000 %s' % (audiofile, speechFile)
        elif cmp(filetype, 'pcm') == 0:
            cmd = 'mv %s %s' % (audiofile, speechFile)
        else:
            return ''
        os.system(cmd)
        if os.path.exists(audiofile):
            #os.remove(audiofile)
            return speechFile
        else:
            return ''

# This class provides the functionality we want. You only need to look at
# this if you want to know how this works. It only needs to be defined
# once, no need to muck around with its internals.
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args:
            self.fall = True
            return True
        else:
            return False
