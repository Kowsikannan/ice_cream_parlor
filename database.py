import sqlite3

# Create a connection to the database
def create_connection():
    conn = sqlite3.connect("my_database.db")
    return conn

# Ensure the database is created (optional)
def create_tables():
    conn = create_connection()
    print("Connected to database successfully.")
    conn.close()
