# init_db.py
import sqlite3

def init_db():
    with sqlite3.connect("db.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE goals (
                goalID INTEGER PRIMARY KEY AUTOINCREMENT,
                goalDescription TEXT NOT NULL,
                completed BOOL NOT NULL
            );
        """)
        cursor.execute("""
            CREATE TABLE history (
                sessionID INTEGER PRIMARY KEY AUTOINCREMENT,
                subject TEXT NOT NULL,
                time_minutes INTEGER NOT NULL,
                date TEXT NOT NULL DEFAULT (DATE('now'))
            );
        """)
        conn.commit()
