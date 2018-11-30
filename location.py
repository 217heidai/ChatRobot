#!/usr/bin/python
# -*- encoding=utf-8 -*- s
# 文件名：location.py


from urllib2 import urlopen
from json import load

from tools import Tools

"""
获取本机公网IP
"""
class PublicIP(object):
    def __init__(self):
        self.__urlPool = {
            'http://jsonip.com': 'ip',
            'http://httpbin.org/ip': 'origin', 
            'https://api.ipify.org/?format=json': 'ip'
        }
        self.__tools = Tools()
    
    def get_IP(self):
        ipList = []
        for url, keyWorld in self.__urlPool.items():
            try:
                ip = load(urlopen(url))[keyWorld]
                if self.__tools.validate_ipv4(ip):
                    ipList.append(ip)
                    break
            except Exception:
                continue
        if len(ipList) > 0:
            return ipList[0]
        else:
            raise Exception('can not get public ip')
"""
IP定位
"""
class Location(object):
    def __init__(self):
        self.__publicIP = PublicIP()

    def get_Location(self):
        ip = self.__publicIP.get_IP()
        request = load(urlopen("http://ip.taobao.com/service/getIpInfo.php?ip={}".format(ip)))
        if request['data']['city'] in ['XX','']:
            raise Exception('can not get public location')
        else:
            country = request['data']['country'] #国家
            province = request['data']['region'] #省份
            city = request['data']['city'] #城市
            return country, province, city