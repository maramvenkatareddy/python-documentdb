from bson import ObjectId
from .db import collection

def serialize_item(item):
    item["id"] = str(item["_id"])
    del item["_id"]
    return item

def create_item(item_data):
    result = collection.insert_one(item_data)
    return serialize_item(collection.find_one({"_id": result.inserted_id}))

def create_items_bulk(items_data):
    result = collection.insert_many(items_data)
    return [serialize_item(collection.find_one({"_id": _id})) for _id in result.inserted_ids]

def get_item(item_id):
    item = collection.find_one({"_id": ObjectId(item_id)})
    return serialize_item(item) if item else None

def get_all_items():
    return [serialize_item(item) for item in collection.find()]

def update_item(item_id, item_data):
    collection.update_one({"_id": ObjectId(item_id)}, {"$set": item_data})
    return serialize_item(collection.find_one({"_id": ObjectId(item_id)}))

def delete_item(item_id):
    return collection.delete_one({"_id": ObjectId(item_id)}).deleted_count
