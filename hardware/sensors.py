# Interface for sensors / camera
# Currently simulates image capture

import cv2

def capture_image(image_path=None):
    """
    Simulate capturing image from camera.
    If image_path is provided, use that (for testing).
    """
    if image_path:
        print(f"[Sensors] Using test image: {image_path}")
        return image_path
    else:
        # In real hardware: capture from camera
        # e.g., cv2.VideoCapture(0).read()
        print("[Sensors] Capturing image from camera (simulated)")
        return "captured_image.jpg"