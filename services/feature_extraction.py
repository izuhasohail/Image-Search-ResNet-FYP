# import torch
# import clip
# from PIL import Image

# device = "cuda" if torch.cuda.is_available() else "cpu"
# model, preprocess = clip.load("ViT-B/32", device=device)

# def extract_features(image_path):
#     image = preprocess(Image.open(image_path)).unsqueeze(0).to(device)
#     with torch.no_grad():
#         features = model.encode_image(image)
#     return features.squeeze().cpu().numpy().tolist()


import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image

# Load Pretrained ResNet-50 Model
device = "cuda" if torch.cuda.is_available() else "cpu"
model = models.resnet50(pretrained=True).to(device)
model.eval()

# Remove the last fully connected layer
model = torch.nn.Sequential(*(list(model.children())[:-1]))

# Define Preprocessing Transform
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

def extract_features(image_path):
    """Extracts ResNet feature vector from an image."""
    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        features = model(image).squeeze()
    
    return features.cpu().numpy().flatten().tolist()  # Convert tensor to list
