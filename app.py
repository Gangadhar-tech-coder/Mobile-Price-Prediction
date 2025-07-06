import tkinter as tk
from tkinter import ttk
import joblib
import numpy as np
model = joblib.load("mobile_price_model.pkl")
scaler = joblib.load("scaler.pkl")
root = tk.Tk()
root.title("Mobile Price Predictor")
root.geometry("700x700")
bg_label = tk.Label(root, bg="indigo")
bg_label.place(relwidth=1, relheight=1)
labels = [
    "Battery Power", "Bluetooth (0/1)", "Clock Speed", "Dual SIM (0/1)", "Front Camera",
    "4G (0/1)", "Internal Memory", "Mobile Depth", "Mobile Weight", "Processor Cores",
    "Primary Camera", "Pixel Height", "Pixel Width", "RAM", "Screen Height",
    "Screen Width", "Talk Time", "3G (0/1)", "Touch Screen (0/1)", "WiFi (0/1)"
]
entries = []
frame = tk.LabelFrame(bg_label, text="Enter Mobile Specifications", font=("Arial", 12, "bold"), bg="white", padx=20, pady=10)
frame.place(relx=0.5, rely=0.05, anchor="n")
for i, label in enumerate(labels):
    lbl = tk.Label(frame, text=label, bg="white", fg="black", font=("Arial", 10))
    lbl.grid(row=i, column=0, sticky="w", padx=10, pady=2)
    entry = ttk.Entry(frame)
    entry.grid(row=i, column=1, padx=10, pady=2)
    entries.append(entry)
result_label = tk.Label(bg_label, text="", font=("Arial", 14), bg="sky blue", fg="blue")
result_label.place(relx=0.5, rely=0.88, anchor="center")
def predict_price():
    try:
        values = [float(e.get()) for e in entries]
        scaled_values = scaler.transform([values])
        pred = model.predict(scaled_values)[0]
        categories = ["Low Cost", "Medium Cost", "High Cost", "Very High Cost"]
        result_label.config(text=f"Predicted Price Range: {categories[pred]}")
    except Exception as e:
        result_label.config(text=f"Error: {e}")
predict_btn = ttk.Button(bg_label, text="Predict", command=predict_price)
predict_btn.place(relx=0.5, rely=0.82, anchor="center")
root.mainloop()
