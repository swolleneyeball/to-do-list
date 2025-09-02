import json, time

with open('data/users.json') as users:
    user_data = json.load(users)
print(user_data)

for user in user_data:
    print(user['name'])

def login(auth):
    print("Initializing...")
    username = input("Please enter your username ->  ")
    if username in user_data:
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
