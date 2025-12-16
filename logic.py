# -*- coding: utf-8 -*-
from datetime import date
from database import get_connection

def add_habit(name):
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO habits (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

def get_habits():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT id, name FROM habits")
    habits = c.fetchall()
    conn.close()
    return habits

def mark_done(habit_id):
    today = str(date.today())
    conn = get_connection()
    c = conn.cursor()
    c.execute(
        "INSERT INTO completions (habit_id, date) VALUES (?, ?)",
        (habit_id, today)
    )
    conn.commit()
    conn.close()

def get_completion_count(habit_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute(
        "SELECT COUNT(*) FROM completions WHERE habit_id = ?",
        (habit_id,)
    )
    count = c.fetchone()[0]
    conn.close()
    return count

