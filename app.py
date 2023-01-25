from flask import Flask, request
from pymongo import MongoClient
from dotenv import load_dotenv
from bson import json_util
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv
import json


load_dotenv()

app = Flask(__name__)

uri = os.getenv("MONGO_DATABASE_URL")
username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")
client = MongoClient(f'mongodb+srv://{username}:{password}@popecluster.vdqwgwk.mongodb.net/?retryWrites=true&w=majority')

db = client['crud']
collection = db['addColl']
doc_count = collection.count_documents({})
print(doc_count)

@app.route("/")
def index():
    data = []
    for item in collection.find():
        data.append(item)
    return json.dumps(data, indent=4, default=json_util.default), 200


if __name__ == '__main__':
    app.run(debug=True)