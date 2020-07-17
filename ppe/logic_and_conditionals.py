""" Exercise for logic and conditionals in Python """

# Use 'if' statement with binary decision 'AND' and 'OR'

active_state = False
login_state = False

decision_login = input(f"Do you want start login? (Y/N):\n").upper()

if decision_login == "Y":
    login_state = True
    print("You are logged in!\n")
elif decision_login == "N":
    print(f"you are not logged in yet...")
else:
    print("You didn't got a valid decision")

decision_activate = input(f"Now, do you want be activated? (Y/N):\n").upper()

if decision_activate == "Y":
    active_state = True
    print("Now you are active!\n")
elif decision_activate == "N":
    print(f"You haven't been activated yet...")
else:
    print("You didn't got a valid decision")

if login_state is True:
    print(f"User logged!\n")
else:
    print(f"Not logged yet...")

if active_state is True:
    print(f"User is active!")
else:
    print(f"User still inactive")

if login_state and active_state is True:
    print(f"You have been enabled successfully!\n")
elif login_state or active_state is not True:
    print(f"You still pending in process... checking\n\n")

if login_state is False:
    print(f"You didn't get in or something went wrong. Try login again\n")
else:
    print(f"Login is OK, no issues here!\n")

if active_state is False:
    print(f"You didn't get activated or something went wrong. Try activate again\n\n")
else:
    print(f"Activation is OK, no issues here!\n\n")

print(f"Process has been done. For new validation, restart the program\n")

active_state = False
login_state = False
