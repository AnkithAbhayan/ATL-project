import pathlib
from src import misc
import json
fullpath = str(pathlib.Path(__file__).parent.absolute())+"/data.json"

def deleteaccount(safety):
    with open(fullpath,"r") as JsonFile:
        data = json.load(JsonFile)
    current_user = data["current_user"]
    print(f"Deleting account of user '{current_user}'. Not the user you wanted? Login with another user using 'usermod -l'")
    trial_password = input("Enter password:")
    if trial_password != data["users"][current_user]["password"]:
        print("Wrong password")
        return
    del data["users"][current_user]
    data["current_user"] = ""
    with open(fullpath,"w") as JsonFile:
        json.dump(data,JsonFile,indent=4)
    print("Command completed successfully.")

def changename(safety):
    with open(fullpath,"r") as JsonFile:
        data = json.load(JsonFile)
    current_user = data["current_user"]
    print(f"Changing name of user '{current_user}'. Not the user you wanted? Login with another user using 'usermod -l'.")
    trial_password = input("Enter password:")
    if trial_password != data["users"][current_user]["password"]:
        print("Wrong password.")
        return
    while True:
        new_name = input("Enter new username:")
        if not new_name:
            print("Please enter a valid username")
        else:
            break
    new_data = {new_name:{"password":data["users"][current_user]["password"]}}
    del data["users"][current_user]
    data["users"].update(new_data)
    data["current_user"] = new_name
    with open(fullpath,"w") as JsonFile:
        json.dump(data,JsonFile,indent=4)
    print("Command completed successfully.")

def changepassword(safety):
    with open(fullpath,"r") as JsonFile:
        data = json.load(JsonFile)
    current_user = data["current_user"]
    print(f"Changing password of user '{current_user}'. Not the user you wanted? Login with another user using 'usermod -l'.")
    trial_password = input(f"current password :")
    if trial_password != data["users"][current_user]["password"]:
        print("Wrong password.")
        return
    while True:
        new_password = input("Enter new password:")
        if not new_password:
            print("Please Enter a valid password.")
        else:
            break
    data["users"][current_user]["password"] = new_password
    with open(fullpath,"w") as JsonFile:
        json.dump(data,JsonFile,indent=4)
    print("Command completed successfully.")

def login(safety):
    with open(fullpath,"r") as JsonFile:
        data = json.load(JsonFile)
    username = input("Enter username:")
    if data["users"].get(username):
        password = input(f"Enter password for user '{username}': ")
        if data["users"][username]["password"] == password:
            data["current_user"] = username
            print("Command completed successfully.")
        else:
            print("Wrong password!")
            return ""
    else:
        print(f"The username '{username}' doesnt exist. Try making a new one by using 'usermod -n'")
        return
    with open(fullpath,"w") as JsonFile:
        json.dump(data,JsonFile,indent=4)
    return username

def makenewaccount(safety):
    with open(fullpath,"r") as JsonFile:
        data = json.load(JsonFile)
    username = input("enter username: ")
    if data["users"].get(username):
        print("username already taken.")
        return ""
    while True:
        password = input("enter password: ")
        if password:
            break
        else:
            print("please enter a password.")
    data["users"].update({username:{"password":password}})
    data["current_user"] = username
    with open(fullpath,"w") as JsonFile:
        json.dump(data,JsonFile,indent=4)
    print("Command completed successfully.")
    return username

def parse(user_input):
    with open(fullpath,"r") as JsonFile:
        data = json.load(JsonFile)
    safety = True
    parsed = user_input.split()
    if len(parsed) > 3:
        print("too many arguments. Enter 'help usermod' for more info.")
        return
    elif len(parsed) < 2:
        print("Not enough arguments.")
        print("\n    "+"\n    ".join(data["help"]["specific_help"]["usermod"]))
        return
    safe_palette = {
        "-force":False,
        "-f":False,
        "-s":True,
        "-safe":True
    }
    usermod_palette = {
        "-l":login,
        "-login":login,
        "-n":makenewaccount,
        "-new":makenewaccount,
        "-d":deleteaccount,
        "-delete":deleteaccount,
        "-cp":changepassword,
        "-changepassword":changepassword,
        "-cn":changename,
        "-changename":changename
    }
    if not usermod_palette.get(parsed[1]):
        print("invalid argument '{parsed[1]}' for [args]. Enter 'help usermod' for more info.")
        return
    if len(parsed) == 3:
        if safe_palette.get(parsed[2]):
            safety = safe_palette[parsed[2]]
        else:
            print(f"Invalid Argument '{parsed[2]}' for [safety]. Enter 'help usermod' for more info.")
            return
    usermod_palette[parsed[1]](safety)

def authenticate():
    with open(fullpath,"r") as JsonFile:
        data = json.load(JsonFile)
    JsonFile.close()
    if data["users"] == {}:
        while True:
            print("No account detected. Make a new one.")
            if (thing:= makenewaccount(False)):
                print()
                return thing
                break
    else:
        if data["current_user"]:
            return data["current_user"]
        else:
            while True:
                print("Please login into an account.")
                if (thing:= login(False)):
                    print()
                    return thing
                    break
            print()
            