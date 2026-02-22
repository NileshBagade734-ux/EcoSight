import tensorflow as tf
import os

# Paths
models_folder = r"C:\Users\Lenovo\Desktop\EcoSight\models"
keras_model_path = os.path.join(models_folder, "waste_classifier.h5")
tflite_model_path = os.path.join(models_folder, "waste_classifier.tflite")

# Ensure the models folder exists
if not os.path.exists(models_folder):
    print(f"📁 Models folder not found, creating: {models_folder}")
    os.makedirs(models_folder)

# Check if the .h5 file exists
if not os.path.exists(keras_model_path):
    raise FileNotFoundError(f"Keras model not found at {keras_model_path}")

# Load Keras model
print("🔄 Loading Keras model...")
model = tf.keras.models.load_model(keras_model_path)
print("✅ Keras model loaded successfully.")

# Convert to TFLite
print("🔄 Converting to TFLite...")
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
print("✅ Model converted to TFLite format.")

# Save the TFLite model
with open(tflite_model_path, "wb") as f:
    f.write(tflite_model)

print(f"✅ TFLite model saved at: {tflite_model_path}")