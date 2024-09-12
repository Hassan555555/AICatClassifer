import torch
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, Dataset
from torchvision import models
from PIL import Image

# Define a simple dataset class
class SimpleDataset(Dataset):
    def __init__(self, cat_images, non_cat_images, transform=None):
        self.cat_images = cat_images
        self.non_cat_images = non_cat_images
        self.transform = transform

    def __len__(self):
        return len(self.cat_images) + len(self.non_cat_images)

    def __getitem__(self, idx):
        if idx < len(self.cat_images):
            image, label = self.cat_images[idx], 1
        else:
            image, label = self.non_cat_images[idx - len(self.cat_images)], 0

        if self.transform:
            image = self.transform(image)

        return image, label

# Data transformations
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

# Load your images (assuming you have PIL images loaded in cat_images and non_cat_images lists)
cat_images = [Image.open(f'cat_images/cat_image_{i}.jpg') for i in range(1,20,1)]
non_cat_images = [Image.open(f'non_cat_images/non_cat_image_{i}.jpg') for i in range(1,20,1)]

dataset = SimpleDataset(cat_images, non_cat_images, transform=transform)
dataloader = DataLoader(dataset, batch_size=4, shuffle=True)

# Load the pre-trained MobileNetV2 model
model = models.mobilenet_v2(pretrained=True)

# Modify the classifier for binary classification
model.classifier[1] = torch.nn.Linear(in_features=1280, out_features=2)

# Define loss function and optimizer
criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Training loop
num_epochs = 5
for epoch in range(num_epochs):
    for images, labels in dataloader:
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

    print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# Save the model after training
torch.save(model.state_dict(), 'model.pth')
print("Model saved to 'model.pth'")

print("Training complete!")
