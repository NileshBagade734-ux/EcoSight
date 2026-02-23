import os
from datetime import datetime
from src.inference.predict import predict  # Your existing predictor
from hardware.routes import get_route_servo
from hardware.servo_driver import move_servo

# --- Test Images Folder ---
TEST_FOLDER = os.path.join(os.path.dirname(__file__), "../../test_images/batch")

# --- Logging Setup ---
LOG_FILE = os.path.join(os.path.dirname(__file__), "../../logs/hardware_test_log.csv")
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
if not os.path.exists(LOG_FILE):
    import csv
    with open(LOG_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "image", "label", "confidence", "entropy", "route", "servo_action"])

# --- Main Test Loop ---
def run_hardware_test():
    images = [f for f in os.listdir(TEST_FOLDER) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
    if not images:
        print(f"❌ No images found in {TEST_FOLDER}")
        return

    for img_name in images:
        img_path = os.path.join(TEST_FOLDER, img_name)
        
        # --- Predict ---
        result = predict(img_path)
        label = result["label"]
        confidence = result["confidence"]
        entropy = result["entropy"]
        route = result["route"]

        # --- Determine Servo Action ---
        servo_pin = get_route_servo(route)
        move_servo(servo_pin)

        # --- Log Result ---
        import csv
        with open(LOG_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), img_name, label, confidence, entropy, route, servo_pin])

        print(f"{img_name} → {label} ({confidence:.2f}) → Route: {route} → Servo: {servo_pin}")

if __name__ == "__main__":
    run_hardware_test()
