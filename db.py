import sqlite3

# connect to database
def connect_db(): 
    return sqlite3.connect("db.db")

# function to insert data
def insert_study_session(subject, duration, date):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO history (subject, time_minutes, date) VALUES (?, ?, ?)", (subject, duration, date))
        conn.commit()

# functions to get data
def get_all_sessions():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT subject, time_minutes, date FROM history ORDER BY date DESC")
        return cursor.fetchall()
