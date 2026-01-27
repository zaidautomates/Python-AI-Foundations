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

## 📂 Project 4: Universal Performance Visualizer (EDA)
**File:** `student_visualizer.py`<br>
**Status:** ✅ Completed (Day 4 Task)

A "Smart" Data Visualization tool that adapts to different datasets and generates boardroom-ready reports.

### 🧠 Advanced Engineering Logic:
* **Universal Loader:** Automatically detects environment (**Google Colab** vs **Local PC**) to switch between "Upload Button" and "File Path Input".
* **Duplicate Resolution:** Uses Logic (`Name + Roll No`) to distinguish between students with identical names, preventing data merging errors.
* **Dynamic Canvas:** Algorithmically adjusts the graph height based on user input (e.g., auto-expands for 50 students vs 10 students).
* **Smart Calculation:** If "Total Marks" are missing in the raw CSV, the script automatically detects numeric subjects and calculates performance metrics on the fly.

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
### 👨‍💻 Author
<b>Zaid Ali</b> | AI Engineer in Making | n8n Developer

<i>Building the bridge between Automation and AI.</i>
