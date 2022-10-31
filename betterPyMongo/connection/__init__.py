import pymongo


class Server:
    def __init__(self, url: str, dbName: str):
        self.client = pymongo.MongoClient(url)
        self.database = self.client[dbName]
    
    def create_collection(self, colName: str):
        return self.database[colName]
    
    def check_collection(self, colName: str):
        if colName not in self.database.list_collection_names():
            return False
        return True
