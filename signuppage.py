import tkinter as tk
from tkinter import messagebox #for displaying messages to user
import sqlite3
import os

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

def switch_to_signin():
    root.destroy()
    os.system("signinpage.py")

# GUI window
root = tk.Tk()
root.title("Sign Up")

# create and place widgets
label_email = tk.Label(root, text="Email:")
label_email.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_email = tk.Entry(root)
entry_email.grid(row=0, column=1, padx=10, pady=5)

label_password1 = tk.Label(root, text="Password:")
label_password1.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_password1 = tk.Entry(root, show="*")
entry_password1.grid(row=1, column=1, padx=10, pady=5)

label_password2 = tk.Label(root, text="Confirm Password:")
label_password2.grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_password2 = tk.Entry(root, show="*")
entry_password2.grid(row=2, column=1, padx=10, pady=5)

button_submit = tk.Button(root, text="Submit", command=submitSignup)
button_submit.grid(row=3, columnspan=2, padx=10, pady=10)

button_switch_to_signin = tk.Button(root, text="Already have an account? Sign in here.", command=switch_to_signin)
button_switch_to_signin.grid(row=4, columnspan=2, padx=10, pady=5)

root.mainloop()