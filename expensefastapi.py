from fastapi import FastAPI
from db_setup import create_table
from crud import create_expense, get_expenses, update_expense, delete_expense

app = FastAPI()

create_table()


@app.get("/")
def home():
    return {"message": "Expense Tracker API Running"}


@app.post("/expenses")
def add_expense(title: str, amount: float, category: str):
    create_expense(title, amount, category)
    return {"message": "Expense added successfully"}

@app.put("/expenses/{expense_id}")
def edit_expense(expense_id: int, title: str, amount: float, category: str):
    update_expense(expense_id, title, amount, category)
    return {"message": "Expense updated successfully"}

@app.delete("/expenses/{expense_id}")
def remove_expense(expense_id: int):
    delete_expense(expense_id)
    return {"message": "Expense deleted successfully"}

@app.get("/expenses")
def list_expenses():
    expenses = get_expenses()
    return {"expenses": [dict(exp) for exp in expenses]}