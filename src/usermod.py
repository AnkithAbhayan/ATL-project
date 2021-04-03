import pathlib
from src import misc
from src.usermod_funcs import login,makenewaccount,deleteaccount,changepassword,changename
import json
fullpath = str(pathlib.Path(__file__).parent.absolute())+"/data.json"

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
        "--force":False,
        "-f":False,
        "-s":True,
        "--safe":True
    }
    usermod_palette = {
        "-l":login.login,
        "--login":login.login,
        "-n":makenewaccount.makenewaccount,
        "--new":makenewaccount.makenewaccount,
        "-d":deleteaccount.deleteaccount,
        "--delete":deleteaccount.deleteaccount,
        "-cp":changepassword.changepassword,
        "--change-password":changepassword.changepassword,
        "-cn":changename.changename,
        "--change-name":changename.changename
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
    usermod_palette[parsed[1]](safety,fullpath)

def authenticate():
    with open(fullpath,"r") as JsonFile:
        data = json.load(JsonFile)
    JsonFile.close()
    if data["users"] == {}:
        while True:
            print("No account detected. Make a new one.")
            if (thing:= makenewaccount.makenewaccount(False,fullpath)):
                print()
                return thing
                break
    else:
        if data["current_user"]:
            return data["current_user"]
        else:
            while True:
                print("Please login into an account.")
                if (thing:= login.login(False,fullpath)):
                    print()
                    return thing
                    break
            print()
            
