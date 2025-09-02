import json, time
usernames = ["Uno","Dos", "Tres", "Quattro", "Cinco"]

def login(auth):
    print("Initializing...")
    time.sleep(2)
    username = input("Please enter your username ->  ")
    if username in usernames:
        print("Welcome back, " + username + "!")
        auth = True
        if auth == True:
            print("Authorized successful.")
        return auth
    else:
        print("Username not recognized.")
        auth = False
        if auth == False:
            print("Unable to authorize.")
            exit()
        return auth

auth_status = login(auth=bool)
print(auth_status)

def to_do_list():
    if auth_status == True:
        print("Accessing to-do list...")
        time.sleep(2)
        print("To-do list accessed.")
        # Further implementation of to-do list functionality goes here
    else:
        print("Access denied. Please log in.")

to_do_list()