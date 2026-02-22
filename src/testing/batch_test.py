import os
import csv
from src.inference.predict import predict  # Your existing predictor
from datetime import datetime

# Folder with batch test images
TEST_FOLDER = os.path.join(os.getcwd(), "test_images", "batch")
LOG_FOLDER = os.path.join(os.getcwd(), "logs")
LOG_FILE = os.path.join(LOG_FOLDER, "predictions.csv")

# Create logs folder if not exists
os.makedirs(LOG_FOLDER, exist_ok=True)

# Check if test folder exists
if not os.path.exists(TEST_FOLDER):
    print(f"❌ Batch folder not found: {TEST_FOLDER}")
    print("Please create this folder and put images inside it for batch testing.")
    exit()

# Get list of images
images = [f for f in os.listdir(TEST_FOLDER) if f.lower().endswith((".jpg", ".jpeg", ".png"))]

if not images:
    print(f"⚠️ No images found in {TEST_FOLDER}. Add some images to test.")
    exit()

print(f"Found {len(images)} images for testing.\n")

# Open CSV log for appending
with open(LOG_FILE, mode="a", newline="") as csv_file:
    fieldnames = ["timestamp", "image_name", "label", "confidence", "entropy", "route"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    # Write header if file is empty
    if os.stat(LOG_FILE).st_size == 0:
        writer.writeheader()
    
    # Run prediction for each image
    for img_name in images:
        img_path = os.path.join(TEST_FOLDER, img_name)
        result = predict(img_path)
        
        # Convert np.float32 to float for logging
        result["entropy"] = float(result["entropy"])
        
        # Print to console
        print(f"{img_name} → {result}")
        
        # Add timestamp and log to CSV
        result["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result["image_name"] = img_name
        writer.writerow(result)

print(f"\n✅ Batch test completed. Results saved to {LOG_FILE}")