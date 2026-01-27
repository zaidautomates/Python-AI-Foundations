import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np

def get_dataset():
    print("\n--- [STEP 1: UPLOAD DATA] ---")
    try:
        from google.colab import files
        print("☁️ Google Colab detected. Upload 'final_report_100.csv' or raw student data.")
        uploaded = files.upload()
        if not uploaded: return None
        return list(uploaded.keys())[0]
    except ImportError:
        return input("💻 Enter CSV file path: ").strip()

def generate_visuals(filepath):
    if not filepath or not os.path.exists(filepath):
        print("❌ Error: Valid file not found.")
        return

    # 1. Load Data
    df = pd.read_csv(filepath)
    total_students = len(df)
    print(f"\n✅ Loaded {total_students} rows.")

    # Check if 'Total' column exists, if not, calculate it
    if 'Total' not in df.columns:
        print("ℹ️ 'Total' column not found. Calculating performance metrics...")
        # Define PASSING_MARKS (can be made configurable)
        PASSING_MARKS = 50 

        # Get numeric columns, excluding potential ID columns
        all_numeric = df.select_dtypes(include=[np.number]).columns.tolist()
        exclude_keywords = ['Roll', 'ID', 'id', 'no', 'No']
        subjects = [col for col in all_numeric if not any(x.lower() in col.lower() for x in exclude_keywords)]

        if not subjects:
            print("❌ Error: Could not detect subject columns for total marks calculation. Make sure your CSV has numeric subject columns.")
            return

        df['Total'] = df[subjects].sum(axis=1)
        df['Percentage'] = df['Total'] / len(subjects)
        df['Status'] = np.where(df['Percentage'] >= PASSING_MARKS, 'Pass', 'Fail')
        print("✅ Performance metrics calculated.")

    # 2. Fix Duplicates: Create Unique Label (Name + Roll)
    # This ensures "Zaid (102)" is different from "Zaid (150)"
    if 'Roll' in df.columns:
        df['Unique_Name'] = df['Name'] + " (" + df['Roll'].astype(str) + ")"
    else:
        df['Unique_Name'] = df['Name'] # Fallback

    # 3. Ask User for N
    while True:
        try:
            val = input(f"How many Toppers? (Max {total_students}): ")
            top_n = int(val)
            if 0 < top_n <= total_students: break
            print(f"Type a number between 1 and {total_students}")
        except ValueError: continue

    # 4. Filter Top N
    top_students = df.sort_values(by='Total', ascending=False).head(top_n)

    # 5. Dynamic Height (Taller graph for more students)
    # Formula: 0.5 inch per student (So 50 students = 25 inches tall)
    fig_height = max(6, top_n * 0.5)
    plt.figure(figsize=(12, fig_height))

    sns.set_theme(style="whitegrid")

    # 6. Plot using UNIQUE NAME
    ax = sns.barplot(x='Total', y='Unique_Name', data=top_students, palette='viridis')

    # 7. Labels on Bars
    for i in ax.containers:
        ax.bar_label(i, fmt='%.1f', padding=3, fontsize=10, fontweight='bold')

    plt.title(f'🏆 Top {top_n} Students (Ranked)', fontsize=16, fontweight='bold')
    plt.xlabel('Total Marks')
    plt.ylabel('Student')
    plt.xlim(0, top_students['Total'].max() * 1.15) # Space for labels

    plt.tight_layout()
    plt.savefig('universal_top_students.png', dpi=300)
    print("✅ Success: Graph saved as 'universal_top_students.png'")
    plt.show()

if __name__ == "__main__":
    csv_file = get_dataset()
    if csv_file:
        generate_visuals(csv_file)
