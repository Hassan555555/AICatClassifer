# Cat vs Non-Cat Image Classifier

## Overview

This project implements an image classification model to distinguish between images of cats and non-cats using PyTorch and a pre-trained MobileNetV2 model. The project includes both training and prediction functionalities.

## Project Structure

- `training.py`: Script to train the MobileNetV2 model with a custom dataset of cat and non-cat images.
- `predict.py`: Script to make predictions on new images using the trained model.
- `cat_images/`: Directory containing cat images used for training.
- `non_cat_images/`: Directory containing non-cat images used for training.
- `test_images/`: Directory containing test images for prediction.

## Requirements

- Python 3.x
- PyTorch
- torchvision
- PIL (Pillow)
- NumPy

You can install the required Python packages using the following command:

```bash
pip install torch torchvision pillow
