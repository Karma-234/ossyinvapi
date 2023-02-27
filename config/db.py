from pymongo import MongoClient
from secretKeys import connectionString 

conn = MongoClient(connectionString)
