# run.py
import sys
import os

# Ensure project root is in Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.inference.predict import predict

# Path to your test image
test_image = os.path.join("test_images", "sample.jpg")

# Run prediction
result = predict(test_image)

print("✅ Prediction Result:")
print(result)