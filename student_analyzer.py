import pandas as pd
import numpy as np

# --- CONFIGURATION ---
FILE_PATH = "student_marks.csv" # Note: Users will update this path for their own machine
PASSING_MARKS = 50

def load_and_inspect_data(filepath):
    print("\n--- [STEP 1: LOADING DATA] ---")
    try:
        df = pd.read_csv(filepath)
        print(f"✅ Success: File loaded.")
        print(f"📊 Dataset Size: {df.shape[0]} Rows, {df.shape[1]} Columns")
        return df
    except FileNotFoundError:
        print(f"❌ Error: File not found at {filepath}.")
        return None

def clean_data(df):
    print("\n--- [STEP 2: DATA CLEANING] ---")
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    averages = df[numeric_cols].mean()
    df_clean = df.fillna(averages)
    print("✅ Data Imputation Complete: Missing values filled with Column Averages.")
    return df_clean

def analyze_performance(df):
    print("\n--- [STEP 3: PERFORMANCE ANALYSIS] ---")
    all_numeric = df.select_dtypes(include=[np.number]).columns.tolist()
    exclude_keywords = ['Roll', 'ID', 'id', 'no', 'No']
    subjects = [col for col in all_numeric if not any(x in col for x in exclude_keywords)]
    
    df['Total'] = df[subjects].sum(axis=1)
    df['Percentage'] = df['Total'] / len(subjects)
    df['Status'] = np.where(df['Percentage'] >= PASSING_MARKS, 'Pass', 'Fail')
    
    topper = df.loc[df['Total'].idxmax()]
    name_col = 'Name' if 'Name' in df.columns else df.columns[0]
    print(f"\n🏆 CLASS TOPPER: {topper[name_col]} with {topper['Total']:.2f} Marks!")
    return df

def save_reports(df):
    print("\n--- [STEP 4: EXPORTING REPORTS] ---")
    df.to_csv("final_report.csv", index=False)
    failed_students = df[df['Status'] == 'Fail']
    if not failed_students.empty:
        failed_students.to_csv("failed_students.csv", index=False)
        print(f"⚠️ Alert: {len(failed_students)} students failed.")
    else:
        print("🎉 No students failed!")

if __name__ == "__main__":
    # Dummy execution for script
    print("To run this, ensure a CSV file exists.")
