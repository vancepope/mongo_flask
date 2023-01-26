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

client = MongoClient(f'mongodb+srv://{username}:{password}@cluster0.1fqhb55.mongodb.net/?retryWrites=true&w=majority')

db = client['store']
collection = db['parts']

@app.get("/")
def index():
    data = []
    for item in collection.find():
        data.append(item)
    if len(data) > 0:
        return json.dumps(data, indent=4, default=json_util.default), 200
    else:
        return json_util.dumps({"error": "Item not found."}), 404

@app.get("/part/<part_id>")
def get_part(part_id):
    part = collection.find_one({"_id": ObjectId(part_id)})
    if part:
        return json_util.dumps(part), 200
    else:
        return json_util.dumps({"error": "Item not found."}), 404

@app.post("/part")
def create_part():
    part = request.get_json()
    result = collection.insert_one(part)
    return json_util.dumps({"_id": str(result.inserted_id)})
    
@app.put("/part/<part_id>")
def update_part(part_id):
    item = request.get_json()
    result = collection.update_one({"_id": ObjectId(part_id)}, {"$set": item})
    if result.matched_count > 0:
        return json_util.dumps({"status": "Success"})
    else: 
        return json_util.dumps({"error": "Item not found"}), 404
    
@app.delete("/delete_part/<part_id>")
def delete_part(part_id):
    result = collection.delete_one({"_id": ObjectId(part_id)})
    if result.deleted_count > 0:
        return json_util.dumps({"status": "Success"}), 200
    else: 
        return json_util.dumps({"error": "Item not found"}), 404
    
if __name__ == '__main__':
    app.run(debug=True)