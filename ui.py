# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import simpledialog, messagebox
import logic

def refresh_list(listbox):
    listbox.delete(0, tk.END)
    for habit_id, name in logic.get_habits():
        count = logic.get_completion_count(habit_id)
        listbox.insert(tk.END, f"{name} | {count}×")

def add_habit(listbox):
    name = simpledialog.askstring("Nový návyk", "Název návyku:")
    if name:
        logic.add_habit(name)
        refresh_list(listbox)

def mark_done(listbox):
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Chyba", "Vyber návyk.")
        return

    habit_name = listbox.get(selected[0]).split("|")[0].strip()
    for habit_id, name in logic.get_habits():
        if name == habit_name:
            logic.mark_done(habit_id)
            break

    refresh_list(listbox)

def start():
    root = tk.Tk()
    root.title("Personal Habit Tracker – Level 2")
    root.geometry("400x350")

    title = tk.Label(root, text="Habit Tracker", font=("Helvetica", 16))
    title.pack(pady=10)

    listbox = tk.Listbox(root, width=40, height=10)
    listbox.pack(pady=10)

    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="Přidat návyk", command=lambda: add_habit(listbox)).grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="Splněno dnes", command=lambda: mark_done(listbox)).grid(row=0, column=1, padx=5)

    refresh_list(listbox)
    root.mainloop()

