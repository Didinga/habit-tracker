# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import simpledialog, messagebox
import logic
import matplotlib.pyplot as plt

# ---------------- UI FUNKCE ----------------
def refresh_list(listbox):
    listbox.delete(0, tk.END)
    for habit_id, name in logic.get_habits():
        count = logic.get_completion_count(habit_id)
        streak = logic.get_streak(habit_id)
        text = f"{name} | {count}× | streak {streak}"
        listbox.insert(tk.END, text)
        index = listbox.size() - 1
        if streak >= 7:
            listbox.itemconfig(index, fg="green")
        elif streak > 0:
            listbox.itemconfig(index, fg="orange")
        else:
            listbox.itemconfig(index, fg="gray")

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

def show_graph(listbox):
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Chyba", "Vyber návyk.")
        return
    habit_name = listbox.get(selected[0]).split("|")[0].strip()
    for habit_id, name in logic.get_habits():
        if name == habit_name:
            # Získání dat pro graf
            conn = logic.get_connection()
            c = conn.cursor()
            c.execute("SELECT date FROM completions WHERE habit_id = ? ORDER BY date", (habit_id,))
            rows = c.fetchall()
            conn.close()
            if not rows:
                messagebox.showinfo("Info", "Žádná data pro graf.")
                return
            dates = [r[0] for r in rows]
            counts = list(range(1, len(dates)+1))
            plt.figure(figsize=(6,4))
            plt.plot(dates, counts, marker='o', color='green')
            plt.title(f"Pokrok návyku: {habit_name}")
            plt.xlabel("Datum")
            plt.ylabel("Počet splnění")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
            break

# ---------------- START UI ----------------
def start():
    root = tk.Tk()
    root.title("Personal Habit Tracker – Level 2")
    root.geometry("500x400")

    title = tk.Label(root, text="Habit Tracker", font=("Helvetica", 16))
    title.pack(pady=10)

    listbox = tk.Listbox(root, width=50, height=12)
    listbox.pack(pady=10)

    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="Přidat návyk", width=15, command=lambda: add_habit(listbox)).grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="Splněno dnes", width=15, command=lambda: mark_done(listbox)).grid(row=0, column=1, padx=5)
    tk.Button(btn_frame, text="Zobraz graf", width=15, command=lambda: show_graph(listbox)).grid(row=0, column=2, padx=5)

    refresh_list(listbox)
    root.mainloop()
