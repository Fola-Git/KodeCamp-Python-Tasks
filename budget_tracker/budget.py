import datetime
from budget_utils import load_transactions, save_transactions, group_by_category

def add_transaction():
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (Food, Transport, Bills): ")
    amount = float(input("Enter amount: "))
    data = load_transactions()
    data.append({"date": date, "category": category, "amount": amount})
    save_transactions(data)
    print("Transaction saved!")

def view_summary():
    data = load_transactions()
    grouped = group_by_category(data)
    print("\nCategory Totals:")
    for cat, amt in grouped.items():
        print(f"{cat}: ${amt:.2f}")

while True:
    print("\n1. Add Transaction\n2. View Summary\n3. Exit")
    choice = input("Choose: ")
    if choice == "1": add_transaction()
    elif choice == "2": view_summary()
    else: break
