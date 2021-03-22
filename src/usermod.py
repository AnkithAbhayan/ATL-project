import pathlib
import json
fullpath = str(pathlib.Path(__file__).parent.absolute())+"/data.json"

def authenticate():
    with open(fullpath,"r") as JsonFile:
        data = json.load(JsonFile)
    if data["users"] == {}:
        return makenewaccount(data)
    else:
        return data["current_user"]

def makenewaccount(data):
    username = input("enter username: ")
    if data["users"].get(username):
        print("username already taken.")
        makenewaccount()
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
    if len(parsed) == 2:
        if safe_palette.get(parsed[2]):
            safety = safe_palette[parsed[2]]
        else:
            print(f"Invalid Argument '{parsed[2]}' for [safety]. Enter 'help usermod' for more info.")
            return
    usermod_palette[parsed[1]](safety)