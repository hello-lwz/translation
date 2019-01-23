# /usr/bin/env python
# coding=utf8

import httplib
import md5
import urllib
import random
import json


class translation2:
    @classmethod
    def translate(self, q):
        appid = 'xx'  # appid
        secretKey = 'xx'  # 密钥
        httpClient = None
        myurl = '/api/trans/vip/translate'
        fromLang = 'en'
        toLang = 'zh'
        salt = random.randint(32768, 65536)
        sign = appid + q + str(salt) + secretKey
        m1 = md5.new()
        m1.update(sign)
        sign = m1.hexdigest()
        myurl = myurl + '?appid=' + appid + '&q=' + urllib.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
            salt) + '&sign=' + sign
        try:
            httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)
            # response是HTTPResponse对象
            response = httpClient.getresponse()
            # print response.read()
            data = json.loads(response.read())
            data = data["trans_result"][0]["dst"]
            return data
        except Exception, e:
            return ' '
        finally:
            if httpClient:
                httpClient.close()
