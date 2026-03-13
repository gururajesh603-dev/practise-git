from fastapi import FastAPI
app = FastAPI()
# sample data
expenses = [
    {"id": 1, "title": "Lunch", "amount": 200, "category": "Food"},
    {"id": 2, "title": "Bus", "amount": 50, "category": "Travel"},
    {"id": 3, "title": "Movie", "amount": 300, "category": "Entertainment"}
]
# 1. List expenses
@app.get("/expenses")
def list_expenses():
    return expenses
# 2. Total spent
@app.get("/expenses/total")
def total_spent():
    total = sum(e["amount"] for e in expenses)
    return {"total_spent": total}
# 3. Highest expense
@app.get("/expenses/highest")
def highest_expense():
    highest = max(expenses, key=lambda x: x["amount"])
    return highest
# 4. Category filter
@app.get("/expenses/category/{category}")
def filter_category(category: str):
    result = [e for e in expenses if e["category"] == category]
    return result