# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class PostPipeline(object): 

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn =sqlite3.connect("post.db")
        self.curr=self.conn.cursor()
    
    def create_table(self):
        self.curr.execute(""" DROP TABLE IF EXISTS celebrity_2019 """)
        self.curr.execute("""create table celebrity_2019(
                    Name text,
                    Role text
                    
                    )""")
    
    def process_item(self, item, spider):

        self.store_db(item)
        return item
    def store_db(self,item):
        self.curr.execute(""" insert into celebrity_2019 values (?,?)""",(
            str(item['Name']),
            str(item['Role'])
            

        ))
        self.conn.commit()


