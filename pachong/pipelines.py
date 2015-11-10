# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

class PachongPipeline(object):
    def process_item(self, item, spider):
        # try:
        #     name=item.get('name')
        #     url=item.get('url')
        #     data=item.get('data')
        #     conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='',db='movie',port=3306,charset='utf8')
        #     cur=conn.cursor()
        #     cur.execute(u'INSERT INTO dianyin(name,url,data) VALUES("%s","%s","%s")'%(name,url,data))
        #     conn.commit()
        #     cur.close()
        #     conn.close()
        #
        # except MySQLdb.Error,e:
        #     with open('log.txt','a') as f:
        #         f.write("Mysql Error %d: %s" % (e.args[0], e.args[1]))
        #         f.write('\n')
        return item
