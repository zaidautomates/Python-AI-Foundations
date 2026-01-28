# 🐍 Python Logic & Data Engineering for AI

This repository documents my journey in the **3-Month AI/ML Training at UET Mardan (KPITB)**. 
My goal is to master the pipeline from **Core Logic** to **Automated Data Science**.

---

## 📂 Project 1: Smart Expense Tracker (CLI)
**File:** `expense_tracker.py`<br>
**Status:** ✅ Completed (Day 1 Task)
* **Focus:** Logic Building & Error Handling.
* **Tech:** Python Lists, Dictionaries, `try-except` blocks.
* **Key Feature:** Custom filtering algorithm to analyze spending habits.

---
### 🛠️ How to Run:
1. Ensure Python is installed.
2. Run the script in your terminal:
```bash
   python expense_tracker.py
```
---

## 📂 Project 2: Student Management System (CRUD)
**File:** `student_management_system.py`<br>
**Status:** ✅ Completed (Day 2 Task)
* **Focus:** Database Simulation & Data Integrity.
* **Tech:** NoSQL-style List of Dictionaries, Strict Input Validation.
* **Key Feature:** Full CRUD operations (Create, Read, Update, Delete) with ID checks.

---
### 🛠️ How to Run:

**Option 1: In Terminal/VS Code**
1. Ensure Python is installed.
2. Run the specific file:
```bash
python student_system.py
```
**Option 2: In Google Colab**<br>
1. Upload the .py file to the Colab "Files" section.<br>
2. Run the command:
```bash
python student_system.py     
```
---

## 📂 Project 3: Automated Student Analyzer (Data Engineering)
**File:** `student_analyzer.py`<br>
**Status:** ✅ Completed (Day 3 Task)
* **Focus:** Automated Data Pipelines & Imputation.
* **Tech:** Pandas for CSV ingestion, NumPy for vectorized stats.
* **Key Feature:** Automatically detects missing values (`NaN`) and fills them with the class average, generating a `failed_students.csv` report.

---
### 🛠️ How to Run:

**Option 1: In Terminal (VS Code)**
```bash
pip install pandas numpy
python student_analyzer.py
```
**Option 2: In Google Colab**

1. Upload your CSV file (e.g., student_marks.csv).
2. Update the FILE_PATH in the script.
3. Run the analysis.

---

## 📂 Project 4: Universal Visualizer (EDA)
**File:** `student_visualizer.py`<br>
**Status:** ✅ Completed (Day 4 Task)
* **Focus:** Data Visualization & Insights.
* **Tech:** **Seaborn** & **Matplotlib**. A smart tool that auto-adjusts graph size and handles duplicate names.
---

### 🛠️ How to Run:

**Option 1: In Terminal (VS Code)**
```bash
pip install pandas matplotlib seaborn
python student_visualizer.py
```
**Option 2: In Google Colab**
1. Run the script.
2. Click the "Choose Files" button when prompted.
3. Enter the number of toppers you want to visualize (e.g., 20 or 50).

---

## 📂 Project 5: Universal ML Predictor (Machine Learning)
**File:** `ml_predictor.py`<br>
**Status:** ✅ Completed (Day 5 Task)

A generic **Supervised Learning** tool that fits a **Linear Regression** model to any dataset.

### 🧠 AI Concepts Applied:
* **Scikit-Learn Implementation:** Used `sklearn.linear_model` to train the AI.
* **Universal Feature Selection:** The script allows users to choose *any* Input (X) and Target (y) column from their CSV.
* **Train-Test Split:** Implemented `train_test_split` (80/20) to validate model accuracy before deployment.
* **Interactive Prediction:** Allows real-time user input to generate future predictions based on learned patterns.

---

### 🛠️ How to Run:
```bash
pip install pandas scikit-learn matplotlib
python ml_predictor.py
```
---

<b>👨‍💻 Author</b> <br>
<b>Zaid Ali</b> | AI Engineer in Making | n8n Developer

<i>Building the bridge between Automation and AI.</i>
