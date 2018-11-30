#!/usr/bin/python
# -*- encoding=utf-8 -*- s
# 文件名：tools.py

import os
import sys
import re

class Tools(object):
    def __init__(self):
        pass
    
    def validate_ipv4(self, ip_str): # ipv4地址合法性判断
        sep = ip_str.split('.')
        if len(sep) != 4:
            return False
        for i,x in enumerate(sep):
            try:
                int_x = int(x)
                if int_x < 0 or int_x > 255:
                    return False
            except ValueError, e:
                return False
        return True
 
    def validate_ipv6(self, ip_str): # ipv6地址合法性判断
        #:Regex for validating an IPv6 in hex notation
        _HEX_RE = re.compile(r'^:{0,1}([0-9a-fA-F]{0,4}:){0,7}[0-9a-fA-F]{0,4}:{0,1}$')
    
        #:Regex for validating an IPv6 in dotted-quad notation
        _DOTTED_QUAD_RE = re.compile(r'^:{0,1}([0-9a-fA-F]{0,4}:){2,6}(\d{1,3}\.){3}\d{1,3}$')
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
