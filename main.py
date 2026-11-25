from fastapi import FastAPI, HTTPException
import pyodbc
import bcrypt
from pydantic import BaseModel, Field

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=Aryan;"
        "DATABASE=EmployeeDB;"
        "Trusted_Connection=yes;"
    )

@app.get("/employees")
def get_employees():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, dept, salary FROM employees")
    rows = cursor.fetchall()
    conn.close()
    return [
        {"id": r.id, "name": r.name, "dept": r.dept, "salary": r.salary}
        for r in rows
    ]

class Employee(BaseModel):
    name: str = Field(min_length=1)
    dept: str = Field(min_length=1)
    salary: int = Field(gt=0)

@app.post("/employees")
def add_employee(emp: Employee):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO employees (name, dept, salary) VALUES (?, ?, ?)",
        emp.name, emp.dept, emp.salary
    )
    conn.commit()
    conn.close()
    return {"message": "Employee added"}

@app.delete("/employees/{emp_id}")
def delete_employee(emp_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employees WHERE id = ?", emp_id)
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Employee not found")
    conn.commit()
    conn.close()
    return {"message": "Employee deleted"}

@app.put("/employees/{emp_id}")
def update_employee(emp_id: int, emp: Employee):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE employees SET name = ?, dept = ?, salary = ? WHERE id = ?",
        emp.name, emp.dept, emp.salary, emp_id
    )
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code= 404, detail="Employee not found")
    conn.commit()
    conn.close()
    return {"message": "Employee updated"}

class LoginData(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(data: LoginData):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT password_hash FROM users WHERE username = ?",
        data.username
    )
    row = cursor.fetchone()
    conn.close()
    if row is None or not bcrypt.checkpw(data.password.encode(), row.password_hash.encode()):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"message": "Login successful"}