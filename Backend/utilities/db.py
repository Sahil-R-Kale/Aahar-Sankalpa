from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

username = os.getenv('DB_ROOT_USERNAME')
password = os.getenv("DB_ROOT_PASSWORD")
host = os.getenv('DB_HOST')

DB_URL = f"mongodb+srv://{username}:{password}@{host}"

client = MongoClient(DB_URL)

db = client["diet-db"]