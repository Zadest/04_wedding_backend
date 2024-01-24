from fastapi import FastAPI
import sqlite3


# Connect to the database
conn = sqlite3.connect('guests.db')
c = conn.cursor()
app = FastAPI()


# Create the guests table if it doesn't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS guests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        surname TEXT,
        email TEXT,
        rsvp TEXT
    )
''')

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Close the database connection
conn.close()
