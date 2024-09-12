import torch
from torchvision import models
from PIL import Image
import torchvision.transforms as transforms

# Define the transformations used during training
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

# Load the pre-trained MobileNetV2 model and modify for binary classification
model = models.mobilenet_v2(pretrained=True)
model.classifier[1] = torch.nn.Linear(in_features=1280, out_features=2)

# Load the saved model weights
model.load_state_dict(torch.load('model.pth'))
model.eval()  # Set the model to evaluation mode

# Function for prediction
def predict_image(image_path):
    # Load and preprocess the image
    image = Image.open(image_path)
    image = transform(image)
    image = image.unsqueeze(0)  # Add batch dimension

    # Perform inference
    with torch.no_grad():
        outputs = model(image)
        _, predicted = torch.max(outputs, 1)

    # Interpret the result
    label = 'cat' if predicted.item() == 1 else 'non-cat'
    return label

# Test on a new image
test_image_path = 'test_images/test_Image_3.png'  # Replace with the path to your test image
result = predict_image(test_image_path)
print(f'The image is classified as: {result}')
