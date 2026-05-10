# =========================================================
# RBLX ACCOUNT HACKER (PRANK VERSION)
# =========================================================

import tkinter as tk
from tkinter import ttk, messagebox
import random
import threading
import time
import string

# =========================================================
# CONFIG
# =========================================================

PASSWORD = "2026RBLXHACK"

# =========================================================
# MAIN WINDOW
# =========================================================

root = tk.Tk()
root.title("RBLX ACCOUNT HACKER")
root.geometry("1400x850")
root.configure(bg="black")

root.bind("<Escape>", lambda e: root.destroy())

# =========================================================
# LOGIN SCREEN
# =========================================================

login_frame = tk.Frame(root, bg="black")
login_frame.pack(expand=True)

title = tk.Label(
    login_frame,
    text="RBLX ACCOUNT HACKER",
    fg="lime",
    bg="black",
    font=("Consolas", 34, "bold")
)

title.pack(pady=20)

user_label = tk.Label(
    login_frame,
    text="USERNAME",
    fg="lime",
    bg="black",
    font=("Consolas", 14)
)

user_label.pack()

user_entry = tk.Entry(
    login_frame,
    bg="black",
    fg="lime",
    insertbackground="lime",
    font=("Consolas", 14),
    width=30
)

user_entry.pack(pady=10)

pass_label = tk.Label(
    login_frame,
    text="PASSWORD",
    fg="lime",
    bg="black",
    font=("Consolas", 14)
)

pass_label.pack()

pass_entry = tk.Entry(
    login_frame,
    show="*",
    bg="black",
    fg="lime",
    insertbackground="lime",
    font=("Consolas", 14),
    width=30
)

pass_entry.pack(pady=10)

status_label = tk.Label(
    login_frame,
    text="",
    fg="red",
    bg="black",
    font=("Consolas", 12)
)

status_label.pack(pady=10)

# =========================================================
# MAIN UI
# =========================================================

main_frame = tk.Frame(root, bg="black")

main_title = tk.Label(
    main_frame,
    text="ACCOUNT RECOVERY TERMINAL",
    fg="lime",
    bg="black",
    font=("Consolas", 28, "bold")
)

main_title.pack(pady=10)

terminal = tk.Text(
    main_frame,
    bg="black",
    fg="lime",
    insertbackground="lime",
    font=("Consolas", 11)
)

terminal.pack(fill="both", expand=True, padx=20, pady=20)

progress = ttk.Progressbar(
    main_frame,
    orient="horizontal",
    length=1100,
    mode="determinate"
)

progress.pack(pady=10)

# =========================================================
# TERMINAL FUNCTIONS
# =========================================================

def write(text, delay=0.01):

    terminal.insert("end", text + "\n")
    terminal.see("end")
    root.update()

    time.sleep(delay)

def random_ip():

    return ".".join(str(random.randint(1, 255)) for _ in range(4))

def random_hash(length=32):

    chars = string.ascii_uppercase + string.digits

    return "".join(random.choice(chars) for _ in range(length))

# =========================================================
# LOGS
# =========================================================

logs = [

    "INITIALIZING TERMINAL...",
    "LOADING SECURE MODULES...",
    "CONNECTING...",
    "ESTABLISHING SESSION...",
    "CHECKING DATABASE...",
    "VERIFYING CONNECTION...",
    "LOADING HASH TABLES...",
    "SCANNING DATA...",
    "READING ACCOUNT INDEX...",
    "VERIFYING STATUS...",
    "SEARCHING ACCOUNT...",
    "CHECKING CLOUD SERVERS...",
    "PINGING DATABASE...",
    "VERIFYING NETWORK...",
    "CHECKING CACHE...",
    "STARTING RECOVERY ENGINE...",
    "READING METADATA...",
    "SCANNING SESSION TOKENS...",
    "ACCESSING ARCHIVE...",
    "CHECKING AUTHENTICATION...",
]

# =========================================================
# MATRIX WINDOW
# =========================================================

def matrix_window():

    win = tk.Toplevel(root)

    win.title("DATA STREAM")
    win.geometry("500x300+50+50")
    win.configure(bg="black")

    txt = tk.Text(
        win,
        bg="black",
        fg="lime",
        font=("Consolas", 10)
    )

    txt.pack(fill="both", expand=True)

    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    while True:

        line = "".join(random.choice(chars) for _ in range(70))

        try:
            txt.insert("end", line + "\n")
            txt.see("end")
            win.update()
        except:
            break

        time.sleep(0.03)

# =========================================================
# MAIN TERMINAL
# =========================================================

def run_terminal():

    threading.Thread(target=matrix_window, daemon=True).start()

    for i in range(101):

        progress["value"] = i

        if i < len(logs):
            write("[SYSTEM] " + logs[i])

        if i % 5 == 0:
            write("[IP] " + random_ip())

        if i % 7 == 0:
            write("[HASH] " + random_hash())

        time.sleep(0.08)

    write("")
    write("==============================================")
    write("ACCESS GRANTED")
    write("==============================================")
    write("")

    time.sleep(2)

    messagebox.showinfo(
        "RBLX ACCOUNT HACKER",
        "ACCESS GRANTED!\n\nUSERNAME:CoolGamer667767\nPASSWORD:\nbaziaylar30baziaylar31ceker"
    )

# =========================================================
# LOGIN FUNCTION
# =========================================================

def login():

    password = pass_entry.get()

    if password == PASSWORD:

        login_frame.pack_forget()

        main_frame.pack(fill="both", expand=True)

        threading.Thread(target=run_terminal, daemon=True).start()

    else:

        status_label.config(text="ACCESS DENIED")

# =========================================================
# LOGIN BUTTON
# =========================================================

login_btn = tk.Button(
    login_frame,
    text="LOGIN",
    command=login,
    bg="black",
    fg="lime",
    font=("Consolas", 14),
    width=20
)

login_btn.pack(pady=20)

# =========================================================
# RUN
# =========================================================

root.mainloop()