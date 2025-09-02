import json, time

with open('data/users.json') as users:
    user_data = json.load(users)

user_list = [user['name'] for user in user_data['users']]
print(user_list)
def login(auth):
    print("Initializing...")
    username = input("Please enter your username ->  ")
    if username in user_list:
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
