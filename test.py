# coding:utf-8
import re
import MySQLdb

# def aaaa(x):
#     return str(x)
name='fef'
url='vvvvv'
data='2015-11-09'
conn=MySQLdb.connect(host="127.0.0.1",user="root",passwd="",db="movie",port=3306,charset='utf8')

cur=conn.cursor()
ss=u"INSERT INTO dianyin(name,url,data) VALUES ( %s,  %s,  %s)" %('fff','aaaa','2015-2-4')
ss2='SELECT * FROM dianyin'
print ss
print cur.execute(ss)
# data=cur.fetchall()
# for i in data:
#     # print map(aaaa,list(i))[2]
#     print i
conn.commit()

cur.close()
conn.close()

