import tkinter as tk
from tkinter import messagebox
import sqlite3

# defining function to handle sign-in
def signin():
    email = entry_email.get()
    password = entry_password.get()

    # connect to db
    conn = sqlite3.connect("login.db")
    cursor = conn.cursor()

    # check for email and password combo in db
    cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = cursor.fetchone()

    if user:
        result_label.config(text="Log in successful.", fg="green")
    else:
        result_label.config(text="Email or password incorrect.", fg="red")

    conn.close()

