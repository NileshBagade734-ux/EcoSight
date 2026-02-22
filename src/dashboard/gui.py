# src/testing/dashboard/gui.py
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
from src.inference.predict import predict  # Your existing predictor
import os
import csv
from datetime import datetime

# --- Logging Setup ---
LOG_FILE = os.path.join(os.path.dirname(__file__), "../../logs/gui_predictions.csv")
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "image", "label", "confidence", "entropy", "route"])

# --- GUI App ---
class EcoSightGUI:
    def __init__(self, master):
        self.master = master
        master.title("EcoSight Live Prediction")
        master.geometry("800x600")
        master.configure(bg="#f0f0f0")

        # --- Widgets ---
        self.img_label = tk.Label(master, bg="#f0f0f0")
        self.img_label.pack(pady=20)

        self.result_label = tk.Label(master, text="", font=("Arial", 16), bg="#f0f0f0")
        self.result_label.pack(pady=10)

        self.upload_btn = tk.Button(master, text="Upload Image", command=self.upload_image, bg="#4caf50", fg="white", font=("Arial", 14))
        self.upload_btn.pack(pady=10)

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            # Display Image
            cv_img = cv2.imread(file_path)
            cv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv_img)
            img = img.resize((400, 400))
            imgtk = ImageTk.PhotoImage(image=img)
            self.img_label.configure(image=imgtk)
            self.img_label.image = imgtk

            # Predict
            result = predict(file_path)
            text = (
                f"Label: {result['label']}\n"
                f"Confidence: {result['confidence']:.3f}\n"
                f"Entropy: {result['entropy']:.3f}\n"
                f"Route: {result['route']}"
            )
            self.result_label.config(text=text)

            # Log
            with open(LOG_FILE, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([datetime.now(), os.path.basename(file_path), result['label'], result['confidence'], result['entropy'], result['route']])

# --- Run App ---
if __name__ == "__main__":
    root = tk.Tk()
    app = EcoSightGUI(root)
    root.mainloop()