import json, time
usernames = ["Uno","Dos", "Tres", "Quattro", "Cinco"]

def login() -> bool:
    print("Initializing...")
    time.sleep(3)
    username = input("Please enter your username: ")
    if username in usernames:
        print("Welcome back, " + username + "!")
        return True
    else:
        print("Username not recognized.")
        return False
