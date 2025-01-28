from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client["ecommerce"]

print("Collections disponibles :", db.list_collection_names())

products = db.products.find().limit(5)
for product in products:
    print(product)
