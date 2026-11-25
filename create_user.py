import bcrypt
from main import get_connection

username = input("Username: ")
password = input("Password: ")

hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

conn = get_connection()
cursor = conn.cursor()
cursor.execute(
    "INSERT INTO users (username, password_hash) VALUES (?, ?)",
    username, hashed
)
conn.commit()
conn.close()

print("User created")