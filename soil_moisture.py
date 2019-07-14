import eel
import sqlite3

conn = sqlite3.connect('soil_moisture.db')

c = conn.cursor()

def create_table():
    c.execute("""CREATE TABLE soil_moisture (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 reading INTEGER
                 )""")

def create(reading):
    with conn:
        c.execute(f'INSERT INTO soil_moisture(reading) VALUES ({reading})')

@eel.expose
def all():
    c.execute("SELECT * FROM soil_moisture")
    return c.fetchall()

eel.init('web')

eel.start('index.html')

conn.close()
