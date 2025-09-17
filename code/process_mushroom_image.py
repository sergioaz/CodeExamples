import clip
import torch
from PIL import Image

# Load CLIP model
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

# Process mushroom image
image = preprocess(Image.open("mushroom.jpg")).unsqueeze(0).to(device)
with torch.no_grad():
    image_features = model.encode_image(image)