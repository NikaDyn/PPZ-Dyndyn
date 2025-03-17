import sqlite3

conn = sqlite3.connect("trains.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS train_routes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        train_number TEXT NOT NULL,
        departure TEXT NOT NULL,
        destination TEXT NOT NULL,
        departure_time TEXT NOT NULL,
        arrival_time TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS train_cars (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        train_number TEXT NOT NULL,
        car_type TEXT NOT NULL,
        seat_count INTEGER,
        FOREIGN KEY (train_number) REFERENCES train_routes (train_number)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS train_tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        train_number TEXT NOT NULL,
        car_id INTEGER NOT NULL,
        passenger_name TEXT NOT NULL,
        seat_number INTEGER NOT NULL,
        price REAL NOT NULL,
        FOREIGN KEY (train_number) REFERENCES train_routes (train_number),
        FOREIGN KEY (car_id) REFERENCES train_cars (id)
    )
''')

conn.close()
