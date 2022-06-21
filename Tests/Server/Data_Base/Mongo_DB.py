from pymongo import MongoClient
class Mongodb:
    # miki
    def search_query(self,key,value):
        cluster = MongoClient("mongodb+srv://test_dev:AtmNf7Iz5BIs0dzc@cluster0.qnr3p.mongodb.net/?retryWrites=true&w=majority")
        db = cluster["trado_qa"]
        collection = db["orders"]
        results = collection.find({key:value})
        for result in results:
            return result["lastName"],result['firstName']


    def search_query2(self,key,value):
        cluster = MongoClient("mongodb+srv://test_dev:AtmNf7Iz5BIs0dzc@cluster0.qnr3p.mongodb.net/?retryWrites=true&w=majority")
        db = cluster["trado_qa"]
        collection = db["orders"]
        results = collection.find({key:value})
        for result in results:
            return result["lastName"]

    def search_query3(self,key,value):
        cluster = MongoClient("mongodb+srv://test_dev:AtmNf7Iz5BIs0dzc@cluster0.qnr3p.mongodb.net/?retryWrites=true&w=majority")
        db = cluster["trado_qa"]
        collection = db["orders"]
        results = collection.find({key:value})
        for result in results:
            return result["lastName"]

    def query(self,col,key,value):
        cluster = MongoClient("mongodb+srv://test_dev:AtmNf7Iz5BIs0dzc@cluster0.qnr3p.mongodb.net/?retryWrites=true&w=majority")
        db = cluster["trado_qa"]
        collection = db["adminusers"]
        results = collection.find({key:value})
        for result in results:
            return result[col]


