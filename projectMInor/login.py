import sqlite3

# Create a database connection and cursor
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create a users table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT
    )
''')

# Function to insert user data into the database
def insert_user(username, password):
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("User inserted successfully.")
    except sqlite3.Error as error:
        print("Error inserting user:", error)

# Sample login form
username = input("Enter username: ")
password = input("Enter password: ")

# Insert the user into the database
insert_user(username, password)

# Close the database connection
conn.close()
