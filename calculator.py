import tkinter as tk

# Fenster erstellen
root = tk.Tk()
root.title("Taschenrechner")

# Variable für Eingabeanzeige
eingabe = ""

# Funktion zum Aktualisieren des Displays


def taste_druck(taste):
    global eingabe
    if taste == "=":
        try:
            ergebnis = str(eval(eingabe))
            eingabe_display.config(text=ergebnis)
            eingabe = ergebnis
        except:
            eingabe_display.config(text="Fehler")
            eingabe = ""
    elif taste == "C":
        eingabe = ""
        eingabe_display.config(text="")
    else:
        eingabe += taste
        eingabe_display.config(text=eingabe)


# Anzeige
eingabe_display = tk.Label(root, text="", width=20, height=2, font=(
    "Arial", 24), bg="white", anchor="e")
eingabe_display.grid(row=0, column=0, columnspan=4)

# Buttons anordnen
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# Buttons erstellen
for (text, row, col) in buttons:
    tk.Button(root, text=text, width=5, height=2, font=("Arial", 18),
              command=lambda t=text: taste_druck(t)).grid(row=row, column=col)

# Hauptloop starten
root.mainloop()
