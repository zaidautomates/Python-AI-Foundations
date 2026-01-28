import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import os

def get_dataset():
    print("\n--- [STEP 1: UPLOAD DATASET] ---")
    try:
        from google.colab import files
        print("☁️ Google Colab detected. Please upload your CSV file.")
        uploaded = files.upload()
        if not uploaded: return None
        return list(uploaded.keys())[0]
    except ImportError:
        return input("💻 Enter CSV file path: ").strip()

def train_and_predict(filepath):
    if not filepath or not os.path.exists(filepath):
        print("❌ Error: Invalid file.")
        return

    # 1. Load Data
    df = pd.read_csv(filepath)
    print(f"\n✅ Data Loaded: {len(df)} rows")
    print("👇 Available Columns:")
    print(df.columns.tolist())

    # 2. Select Features
    print("\n--- [STEP 2: FEATURE SELECTION] ---")
    while True:
        feature_col = input("Enter INPUT Column (X): ").strip()
        target_col = input("Enter TARGET Column (y): ").strip()
        if feature_col in df.columns and target_col in df.columns: break
        print("❌ Error: Columns not found.")

    X = df[[feature_col]]
    y = df[target_col]

    # 3. Train Model
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    print("✅ Model Trained Successfully!")
    print(f"📊 Accuracy: {model.score(X_test, y_test):.2f}")

    # 4. Predict Loop
    print("\n--- [STEP 3: PREDICTION] ---")
    print(f"Type 'exit' to stop.")
    while True:
        val = input(f"\nEnter {feature_col}: ")
        if val.lower() == 'exit': break
        try:
            pred = model.predict([[float(val)]])[0]
            print(f"🔮 Prediction ({target_col}): {pred:.2f}")
        except: print("Invalid number.")

if __name__ == "__main__":
    csv_file = get_dataset()
    if csv_file: train_and_predict(csv_file)
