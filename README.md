#  To-Do App (CLI + GUI)

Ova aplikacija omogućuje korisnicima vođenje jednostavne To-Do liste putem:

- 🖥️ **Konzolnog sučelja (CLI)**
- 🪟 **Grafičkog sučelja (GUI)** pomoću FreeSimpleGUI biblioteke
- 🟦 **Samostalne GUI aplikacije** (`.exe` file u `dist/` folderu – ne zahtijeva Python)

---

##  Sadržaj projekta

- `cli.py` – konzolna verzija aplikacije
- `gui.py` – GUI verzija aplikacije
- `functionsGui.py` – pomoćne funkcije za čitanje/spremanje stavki
- `todos.txt` – tekstualna datoteka s unosima (automatski se stvara)
- `dist/gui.exe` – gotova aplikacija za Windows (GUI verzija bez potrebe za Python-om)

---

##  Kako pokrenuti aplikaciju

###  GUI verzija (iz koda)

Pokreni iz terminala:

```bash
python gui.py
