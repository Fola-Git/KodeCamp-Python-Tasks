import json, os
DATA_FILE = "transactions.json"

def load_transactions():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_transactions(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def group_by_category(transactions):
    summary = {}
    for t in transactions:
        summary[t["category"]] = summary.get(t["category"], 0) + t["amount"]
    return summary
