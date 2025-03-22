# import os
# from services.cloudinary import upload_to_cloudinary
# from services.db import save_image_data
# from services.feature_extraction import extract_features

# IMAGE_FOLDER = "images"  # Your local images folder

# def upload_images():
#     for filename in os.listdir(IMAGE_FOLDER):
#         image_path = os.path.join(IMAGE_FOLDER, filename)
#         cloud_url = upload_to_cloudinary(image_path)  # Upload image to Cloudinary
#         features = extract_features(image_path)  # Extract features


#         save_image_data({"image_url": cloud_url, "features": features})

#         print(f"✅ {filename} uploaded & stored in DB")

# if __name__ == "__main__":
#     upload_images()
#     print("🚀 All images uploaded and stored successfully!")

import os
from services.feature_extraction import extract_features
from services.db import save_image_data
from services.cloudinary import upload_to_cloudinary

IMAGE_FOLDER = "images"  # Local image folder

def upload_images():
    for filename in os.listdir(IMAGE_FOLDER):
        image_path = os.path.join(IMAGE_FOLDER, filename)
        cloud_url = upload_to_cloudinary(image_path)  # Upload to Cloudinary
        features = extract_features(image_path)  # Extract ResNet features

        save_image_data({"image_url": cloud_url, "features": features})
        print(f"✅ {filename} uploaded & stored in DB")

if __name__ == "__main__":
    upload_images()
    print("🚀 All images uploaded and stored successfully!")

