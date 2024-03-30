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