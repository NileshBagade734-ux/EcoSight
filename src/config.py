import os

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Dataset path (your images for training)
DATASET_PATH = os.path.join(BASE_DIR, "dataset", "train")  # only train, no val folder

# Saved model paths
MODEL_PATH = os.path.join(BASE_DIR, "models", "waste_classifier.h5")
TFLITE_PATH = os.path.join(BASE_DIR, "models", "waste_classifier.tflite")

# Training parameters
IMG_SIZE = 224
BATCH_SIZE = 16
EPOCHS = 15

# Waste classes
CLASS_NAMES = ['cardboard', 'glass', 'metal', 'paper', 'plastic']

# Confidence threshold for routing
CONFIDENCE_THRESHOLD = 0.60