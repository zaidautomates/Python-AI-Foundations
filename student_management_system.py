import time

# Global list to store student records (Database)
students = []

def calculate_grade(marks):
    """Helper function to calculate grade based on marks."""
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    else:
        return "F"

def add_student():
    print("\n--- [ADD NEW STUDENT] ---")
    
    # --- VALIDATION 1: Roll Number (Unique & Digits Only) ---
    while True:
        roll_no = input("Enter Roll Number (Digits only): ").strip()
        
        if not roll_no.isdigit():
            print("❌ Error: Roll Number must contain digits only (0-9).")
            continue
        
        # Check for duplicates
        exists = False
        for student in students:
            if student['roll_no'] == roll_no:
                print(f"❌ Error: Roll Number {roll_no} already exists.")
                exists = True
                break
        
        if exists:
            continue
        
        break # Roll Number is valid

    name = input("Enter Name: ").strip()
    dept = input("Enter Department: ").strip()

    # --- VALIDATION 2: Marks (0 to 100) ---
    while True:
        try:
            marks_input = input("Enter Marks (0-100): ")
            marks = float(marks_input)
            
            if marks < 0 or marks > 100:
                print("❌ Error: Marks must be between 0 and 100.")
                continue
            
            break # Marks are valid
        except ValueError:
            print("❌ Error: Invalid input! Please enter a numeric value.")

    # Calculate Grade
    grade = calculate_grade(marks)

    # Create Record (Dictionary)
    record = {
        "roll_no": roll_no,
        "name": name,
        "dept": dept,
        "marks": marks,
        "grade": grade
    }
    
    students.append(record)
    print(f"✅ Success: Student '{name}' added with Grade: {grade}")

def view_students():
    print("\n--- [VIEW ALL STUDENTS] ---")
    if not students:
        print("⚠️ No records found.")
        return

    # Table Header
    print(f"{'Roll No':<10} {'Name':<15} {'Dept':<10} {'Marks':<8} {'Grade'}")
    print("-" * 55)
    
    for student in students:
        print(f"{student['roll_no']:<10} {student['name']:<15} {student['dept']:<10} {student['marks']:<8} {student['grade']}")

def search_student():
    print("\n--- [SEARCH STUDENT] ---")
    search_roll = input("Enter Roll Number to Search: ").strip()
    
    found = False
    for student in students:
        if student['roll_no'] == search_roll:
            print("\n✅ Student Record Found:")
            print(f"Name:       {student['name']}")
            print(f"Department: {student['dept']}")
            print(f"Marks:      {student['marks']}")
            print(f"Grade:      {student['grade']}")
            found = True
            break
    
    if not found:
        print(f"❌ Error: Student with Roll No '{search_roll}' not found.")

def update_marks():
    print("\n--- [UPDATE MARKS] ---")
    search_roll = input("Enter Roll Number to Update: ").strip()
    
    for student in students:
        if student['roll_no'] == search_roll:
            print(f"Current Marks for {student['name']}: {student['marks']}")
            
            # --- VALIDATION 3: Update Marks (0-100) ---
            while True:
                try:
                    new_marks = float(input("Enter New Marks (0-100): "))
                    
                    if new_marks < 0 or new_marks > 100:
                        print("❌ Error: Marks must be between 0 and 100.")
                        continue
                        
                    student['marks'] = new_marks
                    student['grade'] = calculate_grade(new_marks) # Update Grade too
                    print(f"✅ Success: Marks updated. New Grade: {student['grade']}")
                    return
                    
                except ValueError:
                    print("❌ Error: Invalid input! Please enter a numeric value.")
                    
    print(f"❌ Error: Student with Roll No '{search_roll}' not found.")

def delete_student():
    print("\n--- [DELETE STUDENT] ---")
    search_roll = input("Enter Roll Number to Delete: ").strip()
    
    for student in students:
        if student['roll_no'] == search_roll:
            confirm = input(f"Are you sure you want to delete {student['name']}? (y/n): ").lower()
            if confirm == 'y':
                students.remove(student)
                print("✅ Success: Student record deleted.")
            else:
                print("🚫 Operation cancelled.")
            return
            
    print(f"❌ Error: Student with Roll No '{search_roll}' not found.")

def main():
    """Main Program Loop"""
    while True:
        print("\n=== 🎓 STUDENT MANAGEMENT SYSTEM v1.0 ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student Marks")
        print("5. Delete Student")
        print("6. Exit")
        
        choice = input("Select Option (1-6): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_marks()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting Program... Goodbye! 👋")
            break
        else:
            print("❌ Invalid Choice. Please select 1-6.")

if __name__ == "__main__":
    main()