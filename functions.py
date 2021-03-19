import json
import os
import pathlib
import sys
import requests
from time import sleep

def credits(user_input):
	fullpath = str(pathlib.Path(__file__).parent.absolute())+"/data.json"
	with open(fullpath,"r") as JsonFile:
		data = json.load(JsonFile)
	output = data["credits"]
	print("\n".join(output))
	
def introduction():
	fullpath = str(pathlib.Path(__file__).parent.absolute())+"/data.json"
	with open(fullpath,"r") as JsonFile:
		data = json.load(JsonFile)
	output = data["introductory_message"]
	print("\n".join(output))

def total_cases(user_input):
	array = user_input.split()
	if len(array) == 2:
		print("Invalid Argument. Enter a country name as an argument.")
		return
	country = " ".join(array[2:len(array)])
	try:
		r = requests.get("https://api.covid19api.com/dayone/country/"+country+"/status/confirmed")
		data = json.loads(r.text)
		totalcases = str(data[-1]["Cases"])
		printable = ["total cases in "+country+" = "+putcommas(totalcases)]
		print("\n    "+"\n    ".join(printable))
	except:
		print("Invalid country name or Weak Internet connection.")
		
def new_cases(user_input):
	array = user_input.split()
	if len(array) == 2:
		print("Invalid Argument. Enter a country name as an argument.")
		return
	country = " ".join(array[2:len(array)])
	try:
		r = requests.get("https://api.covid19api.com/dayone/country/"+country+"/status/confirmed")
		data = json.loads(r.text)
		newcases = str(data[-1]["Cases"]-data[-2]["Cases"])
		printable = ["new cases (daily) in "+country+" = "+putcommas(newcases)]
		print("\n    "+"\n    ".join(printable))  
	except:
		print("Invalid country name or Weak Internet connection.")
		
def find_definition(user_input):
	array = user_input.split()
	if len(array) == 1:
		print("Invalid Arugment. Enter a word as an argument.")
		return
	name = array[1]
	try:
		response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/"+name)
		data = json.loads(response.text)
	except:
		print("Weak Internet Connection.")
		return
	try:
		for item in data[0]["meanings"]:
			print(item["definitions"][0]["definition"])
	except KeyError:
		print("the word you entered is invalid")
def putcommas(string):
    array = list(string)
    count = 0
    newarray = []
    array.reverse()
    for i in range(1,len(array)+1):
        if i%3==0:
            newarray.append(array[i-3:i])
    count = 0
    for item in newarray:
        for number in item:
            count += 1
    if count != len(array):
        difference = len(array)-count
        newarray.append(array[len(array)-difference:len(array)])
    string = ""
    for item in newarray:
        item.reverse()
    newarray.reverse()
    for i in range(len(newarray)):
        for number in newarray[i]:
            string += number
        if i != len(newarray)-1:
            string += ","
    return string
    
def help_info(user_input):
	fullpath = str(pathlib.Path(__file__).parent.absolute())+"/data.json"
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
			print(f"'{command}' is not a valid argument. Enter 'help' for more info")
			return
	print("\n    "+"\n    ".join(help_msg))
	
def stop(user_input):
	print("Stopping", end="", flush=True)
	for i in range(3):
		sleep(0.05)
		print(".", end="", flush=True)
	sleep(0.05)
	print(".", flush=True)
	sys.exit()
