import sqlite3

train_number = input("Enter train number: ")

conn = sqlite3.connect("trains.db")
cursor = conn.cursor()

tables = ["train_cars", "train_tickets", "train_routes"]

for table in tables:
    print(f'Table: {table}\n')
    cursor.execute(f"SELECT * FROM {table} WHERE train_number='{train_number}'")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    print("-----------------------------------------------------")

conn.close()
