import sqlite3

conn = sqlite3.connect("trains.db")
cursor = conn.cursor()

cursor.executemany('''
    INSERT INTO train_routes (train_number, departure, destination, departure_time, arrival_time) VALUES (?, ?, ?, ?, ?)
''', [
    ("IC125", "Київ", "Львів", "08:00", "14:30"),
    ("RE256", "Львів", "Одеса", "10:15", "22:45"),
    ("NV341", "Харків", "Дніпро", "07:30", "10:00"),
    ("IC789", "Одеса", "Київ", "16:00", "23:15"),
    ("RE654", "Дніпро", "Львів", "12:45", "23:30")
])

cursor.executemany('''
    INSERT INTO train_cars (train_number, car_type, seat_count) VALUES (?, ?, ?)
''', [
    ("IC125", "Плацкарт", 54),
    ("IC125", "Купе", 36),
    ("RE256", "СВ", 18),
    ("NV341", "Плацкарт", 54),
    ("IC789", "Купе", 36)
])

cursor.executemany('''
    INSERT INTO train_tickets (train_number, car_id, passenger_name, seat_number, price) VALUES (?, ?, ?, ?, ?)
''', [
    ("IC125", 1, "Іван Петренко", 12, 450.00),
    ("IC125", 2, "Марія Іваненко", 8, 600.00),
    ("RE256", 3, "Олег Коваленко", 5, 1200.00),
    ("NV341", 4, "Анна Савченко", 27, 350.00),
    ("IC789", 5, "Петро Бондар", 14, 700.00)
])
conn.commit()
conn.close()
