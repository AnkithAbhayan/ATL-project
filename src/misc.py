import pathlib
import json
from time import sleep
import sys

fullpath = str(pathlib.Path(__file__).parent.absolute())+"/data.json"

def credits(user_input):
    with open(fullpath,"r") as JsonFile:
    	data = json.load(JsonFile)
    output = data["credits"]
    print("\n".join(output))

def introduction():
    with open(fullpath,"r") as JsonFile:
        data = json.load(JsonFile)
    output = data["introductory_message"]
    print("\n".join(output))

def help_info(user_input):
    array = user_input.split()
    if len(array) > 2:
	    print("Too many Arguments. Enter 'help' for more info.")
	    return
    with open(fullpath,"r") as JsonFile:
	    data = json.load(JsonFile)
    if len(array) == 1:
	    help_msg = data["help"]["full_help"]
    else:
        command = array[1]
        if data["help"]["specific_help"].get(command):
	        help_msg = data["help"]["specific_help"][command]
        else:
	        print(f"'{command}' is not a valid argument. Enter 'help help' for more info")
	        return
    print("\n    "+"\n    ".join(help_msg))

def stop(user_input):
    parsed = user_input.split()
    print("Stopping", end="", flush=True)
    for i in range(3):
	    sleep(0.05)
	    print(".", end="", flush=True)
    sleep(0.05)
    print(".", flush=True)
    sys.exit()

def parse(user_input,command_palette):
    parsed = user_input.split()
    if not user_input:
        return True
    elif "--help" in parsed and command_palette.get(parsed[0]):
        help_info(f"help {parsed[0]}")
        return True
    return False