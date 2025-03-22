# from pymongo import MongoClient
# from config.config import MONGODB_URI

# client = MongoClient(MONGODB_URI)
# db = client["image_search"]
# collection = db["images"]

# def save_image_data(image_data):
#     collection.insert_one(image_data)

# def get_all_images():
#     return list(collection.find({}, {"_id": 0}))

# def find_similar_images(query_vector, top_n=5):
#     images = collection.find()
#     similarities = [
#         (image, cosine_similarity(query_vector, image["features"]))
#         for image in images
#     ]
#     return sorted(similarities, key=lambda x: x[1], reverse=True)[:top_n]

# def cosine_similarity(vec1, vec2):
#     import numpy as np
#     return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

from pymongo import MongoClient
from config.config import MONGODB_URI
import numpy as np


client = MongoClient(MONGODB_URI)
db = client["image_search"]
collection = db["images"]

def save_image_data(image_data):
    collection.insert_one(image_data)

def get_all_images():
    return list(collection.find({}, {"_id": 0}))

def cosine_similarity(vec1, vec2):
    """Computes cosine similarity between two vectors."""
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def find_similar_images(query_vector, top_n=5):
    """Finds top N similar images based on cosine similarity."""
    images = get_all_images()
    
    similarities = [
        (image["image_url"], cosine_similarity(query_vector, image["features"]))
        for image in images
    ]

    return sorted(similarities, key=lambda x: x[1], reverse=True)[:top_n]