import cloudinary
import cloudinary.uploader
from config import config
from config.config import CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET

print("🚀 Cloudinary setup successful", CLOUDINARY_CLOUD_NAME)
cloudinary.config(
    cloud_name=CLOUDINARY_CLOUD_NAME,
    api_key=CLOUDINARY_API_KEY,
    api_secret=CLOUDINARY_API_SECRET
)

def upload_to_cloudinary(image_path):
    response = cloudinary.uploader.upload(image_path)
    return response["secure_url"]
