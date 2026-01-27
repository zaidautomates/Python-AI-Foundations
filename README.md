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

## 📂 Project 2: Student Management System (CRUD)
**File:** `student_system.py`<br>
**Status:** ✅ Completed (Day 2 Task)
* **Focus:** Database Simulation & Data Integrity.
* **Tech:** NoSQL-style List of Dictionaries, Strict Input Validation.
* **Key Feature:** Full CRUD operations (Create, Read, Update, Delete) with ID checks.

---

## 📂 Project 3: Automated Student Analyzer (Data Engineering)
**File:** `student_analyzer.py`<br>
**Status:** ✅ Completed (Day 3 Task)

A production-grade data pipeline that automates the analysis of large student datasets.

### 🧠 Data Science Concepts Applied:
* **Automated Ingestion:** Uses `Pandas` to read CSV files dynamically.
* **Data Imputation:** Automatically detects missing values (`NaN`) and fills them with the class average (Mean Imputation), ensuring no data is lost.
* **Vectorized Analysis:** Uses `NumPy` for high-speed calculation of totals, percentages, and grades without slow loops.
* **Actionable Reporting:** Automatically generates a separate `failed_students.csv` file for immediate attention.

---

### 🛠️ How to Run:

**Option 1: In Terminal**
```bash
pip install pandas numpy
python student_analyzer.py
```
**Option 2: In Google Colab**
```bash
Upload your CSV file (e.g., student_marks.csv).
Update the FILE_PATH in the script.
Run the analysis.
```
---
### 👨‍💻 Author
<b>Zaid Ali</b> | AI Engineer in Making | n8n Developer

<i>Building the bridge between Automation and AI.</i>
