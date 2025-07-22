import sqlite3
from tkinter import messagebox

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
    
def add_goal(goal):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO goals (goalDescription, completed) VALUES (?, ?)", (goal, "false"))
        conn.commit()
        messagebox.showinfo("Success", f"Goal added!")

def get_all_goals():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT goalDescription FROM goals ORDER BY goalID ASC")
        return cursor.fetchall()
