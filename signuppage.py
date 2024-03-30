import tkinter as tk
from tkinter import messagebox #for displaying messages to user
import sqlite3

# defining function for validating email format
def validateEmail(email):
    return "@" in email and "." in email[email.index("@"):]

# defining function to validate password match
def validatePassword(password1, password2):
    return password1 == password2

# defining function to take care of signup submission
def submitSignup():
    # get email and password from entry
    email = entry_email.get()
    password1 = entry_password1.get()
    password2 = entry_password2.get()

    # validate email format
    if not validateEmail(email):
        messagebox.showerror("Error", "Invalid email address format")
        return
    
    # validate password match
    if not validatePassword(password1, password2):
        messagebox.showerror("Error", "Passwords do not match")
        return
   
    # save user info in db
    conn = sqlite3.connect("login.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (email TEXT, password TEXT)")
    cursor.execute("INSERT INTO users VALUES (?, ?)", (email, password1))
    conn.commit()
    conn.close()
    
    # message provided to user to prove db submission
    messagebox.showinfo("Success", "Sign-up successful!")

