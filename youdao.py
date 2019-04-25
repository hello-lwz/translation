# /usr/bin/env python
# coding=utf8

import httplib
import json
import md5
import urllib
import random


class translation:
    @classmethod
    def translate(self, q):
        appKey = 'xxx'
        secretKey = 'xxx'
        httpClient = None
        myurl = '/api'
        q = q
        fromLang = 'EN'
        toLang = 'zh-CHS'
        salt = random.randint(1, 65536)

        sign = appKey + q + str(salt) + secretKey
        m1 = md5.new()
        m1.update(sign)
        sign = m1.hexdigest()
        myurl = myurl + '?appKey=' + appKey + '&q=' + urllib.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
            salt) + '&sign=' + sign

        try:
            httpClient = httplib.HTTPConnection('openapi.youdao.com')
            httpClient.request('GET', myurl)

            # response是HTTPResponse对象
            response = httpClient.getresponse()
            response = response.read()
            data = json.loads(response)
            return data['web'][0]['value'][0]
        except Exception, e:
            return ' '
        finally:
            if httpClient:
                httpClient.close()



