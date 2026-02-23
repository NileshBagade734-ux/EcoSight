# Main control logic connecting prediction → servo movement

from src.hardware.servo_driver import ServoDriver
from src.hardware.routes import get_route
from src.inference.predict import predict  # Your existing predictor
from src.hardware.sensors import capture_image

class EcoSightController:
    def __init__(self):
        self.servo = ServoDriver()

    def process_waste(self, image_path=None):
        """
        Capture image, predict label, and move servo to route waste
        """
        # Capture or use test image
        img = capture_image(image_path)

        # Predict waste type
        result = predict(img)
        print(f"[Controller] Prediction: {result}")

        # Get routing bin
        bin_name = get_route(result["label"])

        # Move servo
        self.servo.move_servo(bin_name)

        return result, bin_name

# --- Test Run ---
if __name__ == "__main__":
    controller = EcoSightController()
    result, bin_name = controller.process_waste("test_images/sample.jpg")
    print(f"✅ Waste sent to: {bin_name}")
