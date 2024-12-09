import sqlite3

# Connect to SQLite and create the database
conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS flavors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    is_seasonal BOOLEAN
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS ingredients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    stock_level INTEGER NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS suggestions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    flavor_name TEXT NOT NULL,
    allergy_concerns TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS cart (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES flavors (id)
)
""")

conn.commit()
conn.close()

print("Database created successfully!")
