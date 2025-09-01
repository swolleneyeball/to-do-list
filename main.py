import auth
usernames = ["Uno","Dos", "Tres", "Quattro", "Cinco"]

def login() -> bool:
    print("Initializing...")
    username = input(str("Please enter your username: "))
    if username in usernames:
        print("Welcome back, " + username + "!")
        return True
    else:
        print("Username not recognized.")
        return False

if login(True):
    print("Access granted.")
else:
    print("Access denied.")