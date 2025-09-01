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
