import sqlite3
def login_user(username, password):
    insecure_query = f"SELECT * FROM users WHERE username ='{username}' AND password = '{password}'"
    secure_query = "SELECT * FROM users WHERE username = ? AND password = ?"
    print("Database queries structured successfully!")
