# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import logging
import datetime
from weibo import settings
LOG_FORMAT = "%(asctime)s-----------------%(levelname)s--------------------%(message)s"
logging.basicConfig(filename="log.log",level=logging.ERROR,format=LOG_FORMAT)

class WeiboPipeline:
    def __init__(self):
        self.connect = pymysql.connect(
            host = settings.MYSQL_HOST,
            db = settings.MYSQL_DBNAME,
            user = settings.MYSQL_USER,
            passwd = settings.MYSQL_PASSWD,
            charset = 'utf8mb4',
            use_unicode = True
        )
        self.cursor = self.connect.cursor()
    def process_item(self, item, spider):
        try:
            self.cursor.execute("insert into weibo_origin (mblogid) values (%s)",item['mblogid'])
            # self.cursor.execute("insert into weibo_origin ( \
            #     mblogid,created_at,source,content,\
            #     comment_count,attitudes_count,reposts_count,text_legth,\
            #     username,userGender,user_id,followers_count,friends_count,\
            #     statuses_count,verified_type) \
            #     values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(item['mblogid'],item['created_at'],item['source'],item['content'],item['comment_count'], item['attitudes_count'],item['reposts_count'],item['text_legth'],item['username'],item['userGender'],item['user_id'],item['followers_count'],item['friends_count'],item['statuses_count'],item['verified_type']))
            self.connect.commit()
        except Exception as error:
            print(error)
        finally:
            return item
    
    def close_spider(self,spider):
        self.connect.close()
