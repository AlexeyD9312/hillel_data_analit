import csv
from pymongo import MongoClient
uri = "mongodb+srv://aviator171513:jKhPUhDvmXw4ln3D@cluster0.eurz2.mongodb.net/sample_mflix?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
new_db = client["new_database"]
collection = new_db["new_collection"]
with open(r"C:\Users\Home\Desktop\hillel\data an\customers.csv","r") as file:
    reader = csv.DictReader(file)
    data = list(reader)

collection.insert_many(data)
print("dobavleno")

