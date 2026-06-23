from pymongo import MongoClient
import certifi

uri = "mongodb+srv://maddibalaji6_db_user:Admin123@cluster1.4twjgmf.mongodb.net/?appName=Cluster1"

try:
    client = MongoClient(uri, tlsCAFile=certifi.where())
    client.admin.command('ping')
    print(" Connected successfully!")
except Exception as e:
    print(f" {e}")


