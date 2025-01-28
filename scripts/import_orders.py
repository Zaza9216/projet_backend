import pandas as pd
from pymongo import MongoClient

file_path = "data/Orders.csv"

# Lire le fichier CSV avec le bon séparateur
data = pd.read_csv(file_path, sep=";", engine="python")

client = MongoClient("mongodb://localhost:27017/")
db = client["ecommerce"]

db.orders.drop()

data_dict = data.to_dict("records")
db.orders.insert_many(data_dict)

print("Les données de 'orders' ont été importées correctement.")
