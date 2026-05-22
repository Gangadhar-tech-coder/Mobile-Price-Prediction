# 📱 Mobile Price Prediction

> ML classification model that predicts the price range of mobile phones based on technical features.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=python&logoColor=white)

---

## 📌 Overview

**Mobile Price Prediction** classifies mobile phones into 4 price categories (Budget → Premium) using machine learning. Rather than predicting an exact price, the model determines which price bracket a device falls into based on its hardware specs — mimicking how manufacturers actually price devices.

---

## 💰 Price Range Categories

| Class | Label | Price Range |
|-------|-------|-------------|
| 0 | Budget | Low cost |
| 1 | Mid-range | Moderate cost |
| 2 | High-end | High cost |
| 3 | Premium | Very high cost |

---

## ✨ Features

- 📊 **20+ Features Analyzed** — RAM, battery, camera, storage, connectivity, etc.
- 🧹 **Full EDA** — Correlation analysis, feature importance, distribution plots
- 🤖 **Multiple Classifiers** — Logistic Regression, Decision Tree, Random Forest, SVM
- 📈 **Accuracy Metrics** — Confusion matrix, precision, recall, F1-score per class
- 🔮 **Prediction Interface** — Input phone specs and get price category instantly

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.8+ |
| ML | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Notebook | Jupyter Notebook |

---

## 🚀 Getting Started

### Prerequisites

```bash
Python 3.8+
pip
Jupyter Notebook
```

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Gangadhar-tech-coder/Mobile-Price-Prediction.git
cd Mobile-Price-Prediction

# 2. Install dependencies
pip install -r requirements.txt

# 3. Open the notebook
jupyter notebook Mobile_Price_Prediction.ipynb
```

---

## 📁 Project Structure

```
Mobile-Price-Prediction/
├── data/
│   ├── train.csv             # Training dataset (2000 samples)
│   └── test.csv              # Test dataset
├── notebooks/
│   └── Mobile_Price_Prediction.ipynb
├── models/
│   └── classifier.pkl        # Best trained model
├── predict.py                # CLI prediction script
├── requirements.txt
└── README.md
```

---

## 📊 Features Used

| Feature | Description |
|---------|-------------|
| `ram` | RAM in MB |
| `battery_power` | Battery capacity (mAh) |
| `px_height` / `px_width` | Screen resolution |
| `int_memory` | Internal storage (GB) |
| `mobile_wt` | Weight (grams) |
| `n_cores` | Number of processor cores |
| `clock_speed` | Processor speed (GHz) |
| `fc` / `pc` | Front / Primary camera (MP) |
| `four_g` / `three_g` | Connectivity support |
| `touch_screen` | Touchscreen (1/0) |
| `wifi` | Wi-Fi support (1/0) |

---

## 📈 Model Performance

| Model | Accuracy |
|-------|----------|
| Logistic Regression | ~81% |
| Decision Tree | ~83% |
| Random Forest | ~89% |
| SVM | ~96% |

---

## 🔮 Make a Prediction

```python
from predict import predict_price_range

specs = {
    "ram": 3000,
    "battery_power": 4500,
    "px_height": 1920,
    "px_width": 1080,
    "int_memory": 64,
    "n_cores": 8,
    "clock_speed": 2.5,
    "fc": 16,
    "pc": 48,
    "four_g": 1,
    "touch_screen": 1,
    "wifi": 1
}

result = predict_price_range(specs)
print(f"Price Range: {result}")  # e.g., "High-end (Class 2)"
```

---

