import pymongo


class PapersCrawlerPipeline(object):

    def __init__(self, mongo_uri, mongo_db, collection_name):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.collection_name = collection_name

    @classmethod
    def from_crawler(cls, spider):
        # import pdb
        # pdb.set_trace()
        return cls(
            mongo_uri=spider.settings.get('MONGO_URI', 'localhost:27017'),
            mongo_db=spider.settings.get('MONGO_DATABASE', spider.spider.name),
            collection_name=spider.settings.get('COLLECTION_NAME', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        return item
