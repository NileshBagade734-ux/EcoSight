import numpy as np
import tensorflow as tf
from PIL import Image
import math
import src.config as config

# Load TFLite model
interpreter = tf.lite.Interpreter(model_path=config.TFLITE_PATH)
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def preprocess(image_path):
    img = Image.open(image_path).convert("RGB")
    img = img.resize((config.IMG_SIZE, config.IMG_SIZE))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0).astype(np.float32)
    return img

def entropy(probs):
    return -sum(p * math.log(p + 1e-10) for p in probs)

def predict(image_path):
    input_data = preprocess(image_path)
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    output = interpreter.get_tensor(output_details[0]['index'])[0]

    idx = np.argmax(output)
    confidence = float(output[idx])
    ent = entropy(output)

    route = (
        f"bin_{config.CLASS_NAMES[idx]}"
        if confidence >= config.CONFIDENCE_THRESHOLD
        else "manual_review"
    )

    return {
        "label": config.CLASS_NAMES[idx],
        "confidence": round(confidence, 3),
        "entropy": round(ent, 3),
        "route": route
    }