# 📝 Personal Habit Tracker – Level 2

Level 2 Habit Tracker je jednoduchá Python aplikace pro sledování osobních návyků s grafickou uživatelskou plochou (Tkinter) a vizualizací pokroku.

---

## 🚀 Funkce Level 2

- Persistovaná data pomocí **SQLite**  
- Oddělená architektura: `UI / Logic / Database`  
- Přehled návyků s počtem splnění a streaky  
- **Barevné zvýraznění** podle streaku:
  - 🟢 zelená → streak ≥ 7  
  - 🟠 oranžová → aktivní streak  
  - ⚪ šedá → žádná konzistence  
- **Graf pokroku** pro každý návyk (matplotlib)  
- Jednoduché přidávání a označování splněných návyků  

---

## 💻 Screenshoty

## ⚡ Instalace a spuštění

1. Klonuj repozitář:

```bash
git clone https://github.com/Didinga/habit-tracker.git
cd habit-tracker
Nainstaluj závislosti:

bash
Copy code
pip3 install matplotlib
Spusť aplikaci:

bash
Copy code
python3 app.py

