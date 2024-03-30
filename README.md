# Friday-Proj-7
In this project, I have created both a sign-up and a sign-in page for a portal. Once the user **signs up** with an email and password combination, the user can then use the **sign-in** page to log in with that pairing.

## Files
1. `signuppage.py`: This file contains the **sign-up** GUI window. Run the program and the GUI window will appear. A user can then type in their email and input a password for their log-in. Once submitted, this pairing will be saved in the database. If a user already has an account, they can click a button to go to the **sign-in** page.
2. `signinpage.py`: This file contains the **sign-in** GUI window. Run the program and the GUI window will appear. A user can then fill in the entry boxes with their email and password log-in they chose when signing up. If this information matches the saved pairing in the database, the log-in will be successful. If not, the user can attempt to log in again or go to the **sign-up** page to create a log-in.
3. `login.db`: This file is the database holding each email and password pair. The database is used to both store this information from the sign-up window and retrieve it during the sign-in window.