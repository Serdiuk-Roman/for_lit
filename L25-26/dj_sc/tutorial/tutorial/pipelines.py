# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from ../../dj_sc.celery import item_to_db

class TutorialPipeline(object):
    def process_item(self, item, spider):
        # celery task(item)
        return item
