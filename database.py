# -*- coding: utf-8 -*-
import sqlite3

DB = "habits.db"

def get_connection():
    return sqlite3.connect(DB)

def init_db():
    conn = get_connection()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS habits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS completions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        habit_id INTEGER,
        date TEXT
    )
    """)

    conn.commit()
    conn.close()

