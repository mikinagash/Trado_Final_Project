import pymongo


class MongoDB:
    def __init__(self,db,col):
        self.client = pymongo.MongoClient(
"mongodb+srv://test_dev:AtmNf7Iz5BIs0dzc@cluster0.qnr3p.mongodb.net/?retryWrites=true&w=majority")
        self.db = self.client[db]
        self.col = self.db[col]
    def find(self,q=""):
        for i in self.col.find(q):
            print(i)


MongoDB("trado_qa","orders").find()
MongoDB("trado_qa","stores").find()
