import os
from dotenv import load_dotenv

load_dotenv()

# CLOUDINARY_CLOUD_NAME="doon4qkgm"
# CLOUDINARY_API_KEY="735892612685739"
# CLOUDINARY_API_SECRET="49jRAR4VWshrRAC25UaBTjmws9U"
# MONGODB_URI="mongodb+srv://zuhasohail2003:zuha123@imagesearchfyp.vvxwb.mongodb.net/?retryWrites=true&w=majority&appName=ImageSearchFYP"

CLOUDINARY_CLOUD_NAME = os.getenv("CLOUDINARY_CLOUD_NAME")
CLOUDINARY_API_KEY = os.getenv("CLOUDINARY_API_KEY")
CLOUDINARY_API_SECRET = os.getenv("CLOUDINARY_API_SECRET")
MONGODB_URI = os.getenv("MONGODB_URI")