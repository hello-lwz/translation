# encoding:utf-8
from googletrans import Translator

class translation4:
    @classmethod
    def translate(self, q):
		translator = Translator(service_urls=['translate.google.cn'])
		source = q
		try:
			text = translator.translate(source,src='en',dest='zh-cn').text
			return text
		except Exception,e:
			return source
# print translation4.translate('Bac Lieu')