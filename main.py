import os
import tempfile
from flask import Flask, request, jsonify
from flask_cors import CORS
from services.db import save_image_data, find_similar_images
from services.cloudinary import upload_to_cloudinary
from services.feature_extraction import extract_features

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}},supports_credentials=True)  # Allow all origins




@app.route("/search", methods=["POST"])
def search_image():
    file = request.files["file"]
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:
        file.save(temp.name)
        temp_path = temp.name
        
    query_features = extract_features(temp_path)
    similar_images = find_similar_images(query_features)
    os.remove(temp_path)
    
    return jsonify({
        "similar_images": [
            {"url": img[0], "score": round(img[1], 4)} for img in similar_images
        ]
    })

@app.route("/upload", methods=["POST"])
def upload_image():
    file = request.files["file"]
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:
        file.save(temp.name)
        temp_path = temp.name
    
    cloud_url = upload_to_cloudinary(temp_path)
    features = extract_features(temp_path)
    save_image_data({"image_url": cloud_url, "features": features})
    
    os.remove(temp_path)
    return jsonify({"message": "Image uploaded", "url": cloud_url})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


# from flask import Flask, request, jsonify
# from services.db import save_image_data, find_similar_images
# from services.cloudinary import upload_to_cloudinary
# from services.feature_extraction import extract_features
# from flask_cors import CORS
# import tempfile
# import os


# app = Flask(__name__)
# CORS(app, resources={r"/*": {"origins": "*"}})  # ✅ Allow all origins

# @app.route("/search", methods=["POST"])
# def search_image():
#     file = request.files["file"]
    
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:
#         file.save(temp.name)
#         temp_path = temp.name
        
#     query_features = extract_features(temp_path)
#     similar_images = find_similar_images(query_features)
#     os.remove(temp_path)
    
#     return jsonify({
#         "similar_images": [
#             {"url": img[0], "score": round(img[1], 4)} for img in similar_images
#         ]
#     })

# @app.route("/upload", methods=["POST"])
# def upload_image():
#     file = request.files["file"]
    
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:
#         file.save(temp.name)
#         temp_path = temp.name
    
#     cloud_url = upload_to_cloudinary(temp_path)
#     features = extract_features(temp_path)
#     save_image_data({"image_url": cloud_url, "features": features})
    
#     os.remove(temp_path)
#     return jsonify({"message": "Image uploaded", "url": cloud_url})


# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000))
#     app.run(host="0.0.0.0", port=port)















# # from fastapi import FastAPI, UploadFile, File
# # from services.db import save_image_data, find_similar_images
# # from services.cloudinary import upload_to_cloudinary
# # from services.feature_extraction import extract_features
# # from fastapi.middleware.cors import CORSMiddleware
# # import uvicorn
# # import tempfile
# # import os
# # from fastapi.responses import JSONResponse
# # from flask import Flask
# # from flask_cors import CORS

# # app = FastAPI()


# # app.add_middleware(
# #     CORSMiddleware,
# #     allow_origins=["*"],  # Allow all origins for testing
# #     allow_credentials=True,
# #     allow_methods=["*"],  # Allow all HTTP methods
# #     allow_headers=["*"],  # Allow all headers
# # )




# # @app.post("/search/")
# # async def search_image(file: UploadFile = File(...)):
# #     with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:
# #         temp.write(await file.read())
# #         temp_path = temp.name
        
# #     query_features = extract_features(temp_path)
# #     similar_images = find_similar_images(query_features)
# #     os.remove(temp_path)
    
# #     # Assuming each item in similar_images is a tuple like (image_url, similarity)
# #     return {
# #         "similar_images": [
# #             {"url": img[0], "score": round(img[1], 4)}  # Use integer indices
# #             for img in similar_images
# #         ]
# #     }







# # # ✅ Search for similar images
# # # @app.post("/search/")
# # # async def search_image(file: UploadFile = File(...)):
# # #     with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:
# # #         temp.write(await file.read())
# # #         temp_path = temp.name  
    
# # #     query_features = extract_features(temp_path)  # Extract features
# # #     similar_images = find_similar_images(query_features)  # Find similar images
# # #     os.remove(temp_path)  # ✅ Cleanup temp file

# # #     return {
# # #         "similar_images": [
# # #             {"url": img["image_url"], "score": round(img["similarity"], 4)} 
# # #             for img in similar_images
# # #         ]
# # #     }


# # # ✅ Upload image & save in DB
# # @app.post("/upload/")
# # async def upload_image(file: UploadFile = File(...)):
# #     with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:
# #         temp.write(await file.read())
# #         temp_path = temp.name  # Temporary file path
    
# #     cloud_url = upload_to_cloudinary(temp_path)  # Upload to Cloudinary
# #     features = extract_features(temp_path)  # Extract features
# #     save_image_data({"image_url": cloud_url, "features": features})  # Save to DB
    
# #     os.remove(temp_path)  # ✅ Cleanup temp file
# #     return {"message": "Image uploaded", "url": cloud_url}


# # if __name__ == "__main__":
# #     port = int(os.environ.get("PORT", 10000))  # Get Render's assigned port
# #     uvicorn.run(app, host="0.0.0.0", port=port)
