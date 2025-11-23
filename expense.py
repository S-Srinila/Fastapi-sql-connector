from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Expense(BaseModel):
    title:str
    amount:float
    category:str

expenses:List[Expense]=[]

@app.post("/expenses", response_model=Expense)
async def add_expense(expense:Expense):
    expenses.append(expense)
    return expense

@app.get("/expenses", response_model=List[Expense])
async def get_all_expenses():
    return expenses

@app.get("/expenses/highest", response_model=Expense)
async def get_highest_expense():
    if not expenses:
        raise HTTPException(status_code=404, detail="No expense found")
    highest=max(expenses, key = lambda x: x.amount)
    return highest

from db import get_connection
@app.on_event("startup")
async def create_table():
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
        id INT AUTO_INCREMENT PRIMARY KEY,
        description VARCHAR(50),
        amount FLOAT,
        date DATE
        )
        """)
        conn.commit()
        cursor.close()
        conn.close()

    @app.post("/expense")
    def add_expense(expense: Expense):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO expenses (description, amount, date) VALUES (%s, %s, %s)",
            (expense.description, expense.amount, expense.date)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return {"message": "Expense added successfully"}

    # API: Get all expenses
    @app.get("/expenses")
    def get_expenses():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM expenses")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
