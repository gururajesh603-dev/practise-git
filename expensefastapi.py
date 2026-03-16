from fastapi import FastAPI
from db_setup import create_table
from models import Expense
from crud import create_expense, get_expenses, update_expense, delete_expense

app = FastAPI()

create_table()


@app.get("/")
def home():
    return {"message": "Expense Tracker API Running"}


@app.post("/expenses")
def add_expense(expense: Expense):
    create_expense(expense.title, expense.amount, expense.category)
    return {"message": "Expense added successfully"}

@app.put("/expenses/{expense_id}")
def edit_expense(expense_id: int, expense: Expense):
    update_expense(expense_id, expense.title, expense.amount, expense.category)
    return {"message": "Expense updated successfully"}

@app.delete("/expenses/{expense_id}")
def remove_expense(expense_id: int):
    delete_expense(expense_id)
    return {"message": "Expense deleted successfully"}

@app.get("/expenses")
def list_expenses():
    expenses = get_expenses()
    return {"expenses": [dict(exp) for exp in expenses]}