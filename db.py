


# Function to add a guest to the database
def add_guest(cursor,connection, name, surname, email, rsvp):
    cursor.execute('''
        INSERT INTO guests (name, surname, email, rsvp)
        VALUES (?, ?, ?, ?)
    ''', (name, surname, email, rsvp))
    connection.commit()

def get_guests(cursor):
    cursor.execute('''
        SELECT * FROM guests
    ''')
    print(cursor.fetchall())
    return cursor.fetchall()