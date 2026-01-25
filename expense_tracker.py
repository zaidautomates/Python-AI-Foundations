import time

# Global list to store data
expenses = [] 

def add_expense():
    """Adds a new expense to the system with validation."""
    print("\n--- ➕ Add New Expense ---")
    item_name = input("Enter Item Name (e.g., Pizza): ").strip()
    
    # Input Validation
    while True:
        try:
            price_input = input(f"Enter Price for '{item_name}': ")
            price = float(price_input)
            if price < 0:
                print("❌ Price cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("❌ Invalid input! Please enter a numeric value for price.")

    # Category input (hum user se category le rahe hain)
    category = input("Enter Category (Food/Travel/Fees): ").strip().capitalize()

    record = {
        "item": item_name,
        "price": price,
        "category": category,
        "timestamp": time.ctime()
    }
    
    expenses.append(record)
    print(f"✅ Successfully added: {item_name} | {category} | {price} PKR")

def view_all_expenses():
    """Displays ALL expenses."""
    print("\n--- 📊 All Expenses Report ---")
    if not expenses:
        print("⚠️ No expenses recorded yet.")
        return

    print(f"{'ID':<5} {'Item':<15} {'Category':<10} {'Price (PKR)':<12} {'Time'}")
    print("-" * 65)
    
    for index, expense in enumerate(expenses, start=1):
        print(f"{index:<5} {expense['item']:<15} {expense['category']:<10} {expense['price']:<12} {expense['timestamp']}")

def filter_by_category():
    """NEW FEATURE: Shows items and total for a specific category only."""
    print("\n--- 🔍 Search by Category ---")
    if not expenses:
        print("⚠️ No data to search.")
        return
    
    # User se pocho konsi category dekhni hai
    target_category = input("Enter Category to search (e.g., Food): ").strip().capitalize()
    
    found = False
    category_total = 0
    
    print(f"\nScanning for category: '{target_category}'...")
    print(f"{'Item':<15} {'Price (PKR)':<12} {'Time'}")
    print("-" * 45)

    # Sirf woh items print karega jo match karengi
    for expense in expenses:
        if expense['category'] == target_category:
            print(f"{expense['item']:<15} {expense['price']:<12} {expense['timestamp']}")
            category_total += expense['price']
            found = True
            
    if found:
        print("-" * 45)
        print(f"💰 Total spent on {target_category}: {category_total} PKR")
    else:
        print(f"❌ No expenses found for category '{target_category}'.")

def calculate_grand_total():
    """Calculates the sum of EVERYTHING."""
    total = 0
    for expense in expenses:
        total += expense['price']
    
    print(f"\n💰 Grand Total Spending: {total} PKR")

def main():
    print("🤖 Zaid's Pro Expense Tracker (v2.0)")
    
    while True:
        print("\nMENU:")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Check Grand Total")
        print("4. Filter by Category (New!)")  # Naya Feature
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_all_expenses()
        elif choice == '3':
            calculate_grand_total()
        elif choice == '4':
            filter_by_category() # Naye function ko call kia
        elif choice == '5':
            print("Exiting... Stay Productive, Zaid! 🚀")
            break
        else:
            print("❌ Invalid selection.")

if __name__ == "__main__":
    main()