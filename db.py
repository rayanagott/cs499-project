import sqlite3
from tkinter import messagebox

# connect to database
def connect_db(): 
    return sqlite3.connect("db.db")

# goals tab queries    
def add_goal(goal):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO goals (goalDescription, completed) VALUES (?, ?)", (goal, "false"))
        conn.commit()
        messagebox.showinfo("Success", f"Goal added!")

def delete_goal(goal_id):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM goals WHERE goalID = ?", (goal_id,))
        conn.commit()

def toggle_goal_completion(goal_id, completed):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE goals SET completed = ? WHERE goalID = ?", (int(completed), goal_id))
        conn.commit()

# history data
def get_all_goals():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT goalID, goalDescription, completed FROM goals ORDER BY goalID ASC")
        return cursor.fetchall()
    
def get_completed_goals():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT goalID, goalDescription, completed FROM goals WHERE completed = 1 ORDER BY goalID ASC")
        return cursor.fetchall()

def insert_study_session(subject, duration, date):
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO history (subject, time_minutes, date) VALUES (?, ?, ?)", (subject, duration, date))
        conn.commit()

def get_study_sessions():
    with connect_db() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT subject, time_minutes FROM history ORDER BY date DESC")
        return cursor.fetchall()



