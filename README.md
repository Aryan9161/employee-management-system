# Employee Management System

A full-stack CRUD app to manage employees, with a login system. Built as a learning project.

## Features
- Login checked by an API (passwords stored as bcrypt hashes)
- View, add, edit and delete employees
- Data saved in SQL Server
- Input validation (no empty name, salary must be above 0)

## Tech Stack
- Frontend: HTML, CSS, JavaScript
- Backend: Python, FastAPI
- Database: SQL Server

## How to run
1. Install packages:
   ```
   pip install fastapi uvicorn pyodbc bcrypt
   ```
2. In SQL Server, create a database `EmployeeDB` with an `employees` table (id, name, dept, salary) and a `users` table (id, username, password_hash).
3. Change the `SERVER=` name in `main.py` to your own SQL Server name.
4. Create a login user:
   ```
   python create_user.py
   ```
5. Start the API:
   ```
   python -m uvicorn main:app --reload
   ```
6. Open `index.html` in your browser and log in.

## API
- `GET /employees`, `POST /employees`
- `PUT /employees/{id}`, `DELETE /employees/{id}`
- `POST /login`
