from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Calculator API is running"}
@app.get("/hello")
def say_hello(name: str):
    return {
        "message": f"Hello {name}, welcome to FastAPI!"
    }
# Addition
@app.get("/add")
def add(a: float, b: float):
    result = a + b
    return {
        "operation": "addition",
        "a": a,
        "b": b,
        "result": result
    }
# Subtraction
@app.get("/subtract")
def subtract(a: float, b: float):
    result = a - b
    return {
        "operation": "subtraction",
        "a": a,
        "b": b,
        "result": result
    }
# Multiplication
@app.get("/multiply")
def multiply(a: float, b: float):
    result = a * b
    return {
        "operation": "multiplication",
        "a": a,
        "b": b,
        "result": result
    }
# Division
@app.get("/divide")
def divide(a: float, b: float):
    if b == 0:
        return {"error": "Division by zero is not allowed"}
    result = a / b
    return {
        "operation": "division",
        "a": a,
        "b": b,
        "result": result
    }