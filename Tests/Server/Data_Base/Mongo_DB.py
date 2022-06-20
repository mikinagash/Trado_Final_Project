import pymongo
class MongoDB:
    def __init__(self):
        self.client = pymongo.MongoClient(
"mongodb+srv://test_dev:AtmNf7Iz5BIs0dzc@cluster0.qnr3p.mongodb.net/?retryWrites=true&w=majority")
        self.db = self.client['trado_qa']

    def collection(self, col):
        self.collection = self.db[col]
        return self.collection


class Queries(MongoDB):
    def find_all(self, col):
        self.collection(col)
        for i in col:
            print(i)



    def find_one(self, col, key1):
        self.collection()
        return key1

    def find_one12(self, col,key1, key2):
        pass

a = Queries()
a.find_all('orders')