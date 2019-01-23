# -*- coding: utf-8 -*-
import MySQLdb as mdb
import json
import time
#有道官方翻译
from youdao import translation
#百度官方翻译
from baidu import translation2
#有道post翻译
from youdao3 import translation3
#google翻译
from google import translation4

def main():
    conn = mdb.connect(
        host='xxxxx',
        port=3306,
        user='xxxx',
        passwd='xxx',
        db='xxxxx',
        charset='utf8'
    )
    cursor=conn.cursor()
    cursor.execute('select id,city,province,country_en from cv')
    cvs = cursor.fetchall()
    begin = time.time()
    for cv in cvs:
        new_regions = []
        id = cv[0]
        old_regions = cv[1:4]
        for old_region in old_regions:
            if old_region and old_region != 'NULL':
				# 这里使用百度翻译
                new_region = translation2.translate(old_region)
                new_region = json.dumps(new_region, encoding='UTF-8', ensure_ascii=False).encode('utf-8')
                new_regions.append(new_region)
            elif old_region == 'NULL':
                new_regions.append(old_region)
            else:
                new_regions.append(None)
        city_cn, province_cn,country_cn = new_regions[0], new_regions[1],new_regions[2]
        print city_cn,province_cn,country_cn, id
        sql = "update cv set city_cn=%s,province_cn=%s,country_cn=%s where id = %s"
        param = (city_cn, province_cn,country_cn,id)
        try:
            cursor.execute(sql,param)
        except:
            conn.rollback()
    conn.commit()
    end = time.time()
    print end-begin
    print '------------------------end-------------------'
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()
