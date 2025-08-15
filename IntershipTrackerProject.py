print("    [ Welcome to the Tracker Expenses System ]    \n")

#===========================================================
#Expense Tracker Application
#Allows user to add , view , update , delete expenses
#and calculate totals [ Overall and Per Category ]
#Data is persisted in a local text file
#===========================================================

expenses_data = {}
next_expense_id = 1
expenses_file_path = "test.txt"

def write_expenses_to_file():
    """
    1)this Function Job is to save all expenses from  expenses_data to the expenses_file_path
    2)format = id|name|amount|category|unit_price
    3)values separated by '|'

    """
    with open(expenses_file_path, 'w', encoding="utf-8") as f:
        for key, value in expenses_data.items():
            # Turn expense data into  = id|name|amount|category|unit_price for saving
            line = f"{key}|{value['name']}|{value['amount']}|{value['category']}|{value['unit_price']}\n"
            f.write(line)

def load_expenses_from_file():
    """
    1)this Function Job is to load all expenses from  the file into the expenses_data dictionary
    2)for handling errors : If the file doesn't exist, it will start with an empty dictionary
    3)Also update the next_expense_id so new expenses get unique IDs

    """
    global expenses_data, next_expense_id
    expenses_data = {}
    try:
        with open(expenses_file_path, "r", encoding="utf-8") as f:
            for line in f:
                #split the line  into individual parts (id , name , amount , category , unit_price)
                line_parts = [p.strip() for p in line.strip().split("|")]

                #skip the line if it doesn't have exactly 5 parts  , 5 parts = id , name , amount , category , unit_price
                if len(line_parts) != 5:
                    continue
                exp_id, expense_name, expense_amount, expense_category, expense_unit_price = line_parts

                try:
                    #convert string values to correct number types
                    exp_id = int(exp_id)
                    expense_amount = int(expense_amount)
                    expense_unit_price = float(expense_unit_price)
                except ValueError:
                    #skip the line if any number is invalid to handle errors
                    continue
                #Store the expense in the dictionary
                expenses_data[exp_id] = {
                    "name": expense_name,
                    "amount": expense_amount,
                    "category": expense_category,
                    "unit_price": expense_unit_price,
                }
    except FileNotFoundError:
        #if no file found = no expenses nave been saved yet
        expenses_data = {}
    #Update the ID tracker so new expenses get the next available ID
    next_expense_id = (max(expenses_data.keys()) + 1) if expenses_data else 1

def show_menu():
    """Display the main menu options"""
    print("1. Enter a new Expense :  ")
    print("2. View All Expenses :  ")
    print("3. Update Expenses :  ")
    print("4. Delete Expenses :  ")
    print("5. Calculate Total Spent :")
    print("6. Calculate Spent by Category :")
    print("0. Exit :  ")

def add_expense():
    """
    this function ask the user for expense details ( name , amount, category , unit_price )
    then save it to the file

    """
    load_expenses_from_file()
    global next_expense_id

    #Get and validate expense name
    name = input("Expense name: ").strip()
    if len(name) < 2 or not any(c.isalpha() for c in name):
        print("❌ Invalid name. Must have at least 2 characters and include letters.")
        return

    #Get and validate amount
    try:
        amount = int(input("Expense amount: ").strip())
        if amount < 1:
            print("❌ Amount cannot be negative or Zero.")
            return
    except ValueError:
        print("❌ Invalid amount. Must be a number")
        return

    #Get and validate category
    category = input("Expense category: ").strip().lower()
    if len(category) < 2 or not any(c.isalpha() for c in category):
        print("❌ Invalid category. Must be at least 2 characters and include letters.")
        return

    #Get and validate unit price
    try:
        unit_price = float(input("Expense unit price: ").strip())
        if unit_price < 1:
            print("❌ Unit price cannot be negative or Zero.")
            return
    except ValueError:
        print("❌ Invalid unit price. Must be a number.")
        return

    #Save the new expense in the dictionary
    expenses_data[next_expense_id] = {
        "name" : name,
        "amount" : amount,
        "category" : category,
        "unit_price" : unit_price
    }

    print(f"ID added {next_expense_id}")
    next_expense_id += 1
    write_expenses_to_file()

def view_expense():
    """
    this function load all expenses from the file and display them to the user one by one
    including a total sum of all expenses

    """
    load_expenses_from_file()
    print(f"Loaded {len(expenses_data)} expense(s).")
    if not expenses_data:
        print("No expenses found")
        return

    print("Total Expenses")
    grand_total = 0

    for expense_id, expense_record in expenses_data.items():
        #Calculate the total cost for this expense (amount * unit price)
        line_total = expense_record["amount"] * expense_record["unit_price"]
        grand_total += line_total

        print(f"ID : {expense_id}")
        print(f"Name :  {expense_record['name']}")
        print(f"category : {expense_record['category']}")
        print(f"amount : {expense_record['amount']}")
        print(f"unit price : {expense_record['unit_price']}")
        print(f"Total for this expense: {line_total}")
        print()

    print(f"Grand Total: {grand_total}")

def update_expense():
    """
    this function let the user choose an expense by ID and then pick a field to update
    validates new values before saving changes to handle any possible error


    """
    load_expenses_from_file()

    #Ask for expense id to update it
    try:
        expense_id = int(input("Enter the expense ID to update: "))
    except ValueError:
        print("❌ Invalid ID. Please enter a number.")
        return

    if expense_id not in expenses_data:
        print(f"❌ Expense with ID {expense_id} not found.")
        return

    expense_record = expenses_data[expense_id]
    print("\nCurrent details:")
    print(f"1. Name       : {expense_record['name']}")
    print(f"2. Amount     : {expense_record['amount']}")
    print(f"3. Category   : {expense_record['category']}")
    print(f"4. Unit Price : {expense_record['unit_price']}")

    choice = input("\nWhich field do you want to update? (name/amount/category/unit_price): ").strip().lower()


    if choice == "name":
        updated_value = input("Enter new name: ").strip()
        if len(updated_value) < 2 or not any(c.isalpha() for c in updated_value):
            print("❌ Invalid name. Must have at least 2 characters and include letters.")
            return
        expense_record["name"] = updated_value
    elif choice == "amount":
        try:
            updated_value = int(input("Enter new amount: "))
            if updated_value <= 0:
                print("❌ Amount must be greater than zero.")
                return
            expense_record["amount"] = updated_value
        except ValueError:
            print("❌ Invalid amount. Must be a number.")
            return
    elif choice == "category":
        updated_value = input("Enter new category: ").strip().lower()
        if len(updated_value) < 2 or not any(c.isalpha() for c in updated_value):
            print("❌ Invalid category. Must be at least 2 characters and include letters.")
            return
        expense_record["category"] = updated_value
    elif choice == "unit_price":
        try:
            updated_value = float(input("Enter new unit price: "))
            expense_record["unit_price"] = updated_value
        except ValueError:
            print("❌ Invalid unit price. Must be a number.")
    else:
        print("❌ Invalid field name. Nothing updated.")
        return

    print(f"✅ Expense ID {expense_id} updated successfully.")
    write_expenses_to_file()

def delete_expense():
    """
    This function remove an expense from the data using its ID
    ask for confirmation before deleting to make sure the user wants to proceed

    """
    load_expenses_from_file()

    try:
        expense_id = int(input("Enter the expense ID to delete: ").strip())
    except ValueError:
        print("❌ Invalid ID.")
        return

    if expense_id not in expenses_data:
        print(f"❌ Expense with ID {expense_id} not found.")
        return

    confirm = input(f"Are you sure you want to delete ID {expense_id}? (y/n): ").strip().lower()
    if confirm != "y":
        print("Canceled.")
        return

    del expenses_data[expense_id]
    write_expenses_to_file()
    print(f"✅ Expense ID {expense_id} deleted.")

def calculate_total_expenses():
    """
        This function calculate and display the sum of all expenses
        if unit price exists = multiply amount * unit price for each expense

    """
    load_expenses_from_file()
    total = 0.0
    for expense_record in expenses_data.values():
        try:
            total += float(expense_record["amount"]) * float(expense_record["unit_price"])
        except (KeyError, TypeError, ValueError):
            continue
    print(f"Total Spent: {round(total, 2)}")

def calculate_expenses_by_category():
    """
      Calculate and display the total amount spent in each category.
    """

    load_expenses_from_file()
    totals = {}
    for expense_record in expenses_data.values():
        expense_category = str(expense_record.get("category", "")).strip().lower() or "uncategorized"
        try:
            category_total = float(expense_record["amount"]) * float(expense_record["unit_price"])
        except (KeyError, TypeError, ValueError):
            continue
        totals[expense_category] = totals.get(expense_category, 0.0) + category_total

    if not totals:
        print("No expenses found.")
        return

    print("\n--- Spent by Category ---")
    for expense_category in sorted(totals):
        print(f"{expense_category}: {round(totals[expense_category], 2)}")
    print(f"\nGrand Total: {round(sum(totals.values()), 2)}")

#Main loop for the application keeps showing the menu until the user exits
while True:
    show_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expense()
    elif choice == "3":
        update_expense()
    elif choice == "4":
        delete_expense()
    elif choice == "5":
        calculate_total_expenses()
    elif choice == "6":
        calculate_expenses_by_category()
    elif choice == "0":
        exit()
    else:
        print("❌ Invalid choice. Try again.")
