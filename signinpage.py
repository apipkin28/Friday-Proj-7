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

# GUI window
root = tk.Tk()
root.title("Sign In")

# create and place widgets
label_email = tk.Label(root, text="Email:")
label_email.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_email = tk.Entry(root)
entry_email.grid(row=0, column=1, padx=10, pady=5)

label_password = tk.Label(root, text="Password:")
label_password.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_password = tk.Entry(root, show="*")  # asterisks for password
entry_password.grid(row=1, column=1, padx=10, pady=5)

button_signin = tk.Button(root, text="Sign In", command=signin)
button_signin.grid(row=2, columnspan=2, padx=10, pady=10)


