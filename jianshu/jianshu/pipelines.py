# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class JianshuPipeline(object):
    # 初始化方法中获取数据库的连接
    def __init__(self):
        dbparam = {
            'host':'127.0.0.1',
            'port':3306,
            'user':'root',
            'password':'smh8532557',
            'database':'zoo',
            'charset':'utf8'
        }
        # 在函数调用时两个**代表关键字参数解包操作
        self.conn = pymysql.connect(**dbparam)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        try:
            sql = "insert into article (title, name, url, collection) values (%s, %s, %s, %s)"
            self.cursor.execute(sql, (item['title'], item['name'], item['url'], item.get('collection', '无专题收入')))
            self.conn.commit()
        except:
            print(Exception)
            print('入库失败')
            self.conn.rollback()
        return item

    def __del__(self):
        self.conn.close()