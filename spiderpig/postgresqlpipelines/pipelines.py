from .sql import Sql
from spiderpig.items import NovelItem, ContentItem

class SpiderpigPipeline(object):

    def process_item(self, item, spider):
        if isinstance(item, NovelItem):
            Sql.insert_novel_info(
                item['name'],
                item['author'],
                item['novelurl'],
                item['serialstatus'],
                item['serialnumber'],
                item['category']
            )

            print("开始存入标题，分类等信息...")

        elif isinstance(item, ContentItem):
            Sql.insert_novel_content(
                item['novelurl'],
                item['chaptername'],
                item['chapterurl'],
                item['chaptercontent'],
                item['chapterorder']
            )

            print("正在存储章节内容...")
        else:
            pase
