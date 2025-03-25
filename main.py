import os
import tempfile
from flask import Flask, request, jsonify
from flask_cors import CORS
from services.db import save_image_data, find_similar_images
from services.cloudinary import upload_to_cloudinary
from services.feature_extraction import extract_features

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}},supports_credentials=True)  # Allow all origins




@app.route("/api/search", methods=["POST"])
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

@app.route("/api/upload", methods=["POST"])
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
