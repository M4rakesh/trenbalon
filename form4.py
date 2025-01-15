import sqlite3
import tkinter as tk
from tkinter import messagebox
import treneri from treneris1
def izveidot_galveno_logu():
    def sportisti_poga():
        sportistu_logs()

    def treneru_poga():
        treneru_logs()

    def apmeklejumi_poga():
        messagebox.showinfo("Apmeklējumi", "Atvērta apmeklējumu pārvaldība.")

    logs = tk.Tk()
    logs.title("Trenažieru zāles pārvaldība")
    logs.geometry("300x200")

    sportisti_btn = tk.Button(logs, text="Sportisti", command=sportisti_poga, width=20, height=2, bg="lightblue")
    sportisti_btn.pack(pady=10)

    treneri_btn = tk.Button(logs, text="Treneri", command=treneru_poga, width=20, height=2, bg="lightgreen")
    treneri_btn.pack(pady=10)

    apmeklejumi_btn = tk.Button(logs, text="Apmeklējumi", command=apmeklejumi_poga, width=20, height=2, bg="lightyellow")
    apmeklejumi_btn.pack(pady=10)

    logs.mainloop()


if __name__ == "__main__":
    izveidot_galveno_logu()