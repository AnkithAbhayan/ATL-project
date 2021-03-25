import json
import os
import pathlib
from src import misc
import requests

fullpath = str(pathlib.Path(__file__).parent.absolute())+"/data.json"

def total_cases(user_input):
    with open(fullpath,"r") as JsonFile:
        data = json.load(JsonFile)
    array = user_input.split()
    if len(array) == 1:
        print("Invalid Argument. Enter a country name as an argument.")
        print("\n    "+"\n    ".join(data["help"]["specific_help"]["total_cases"]))
        return
    country = " ".join(array[1:len(array)])
    try:
        r = requests.get("https://api.covid19api.com/dayone/country/"+country+"/status/confirmed")
        data = json.loads(r.text)
        totalcases = str(data[-1]["Cases"])
        printable = ["total cases in "+country+" = "+putcommas(totalcases)]
        print("\n    "+"\n    ".join(printable))
    except:
        print("Invalid country name or Weak Internet connection.")

def new_cases(user_input):
    with open(fullpath,"r") as JsonFile:
        data = json.load(JsonFile)
    array = user_input.split()
    if len(array) == 1:
        print("Invalid Argument. Enter a country name as an argument.")
        print("\n    "+"\n    ".join(data["help"]["specific_help"]["new_cases"]))
        return     
    country = " ".join(array[1:len(array)])
    try:
        r = requests.get("https://api.covid19api.com/dayone/country/"+country+"/status/confirmed")
        data = json.loads(r.text)
        newcases = str(data[-1]["Cases"]-data[-2]["Cases"])
        printable = ["new cases (daily) in "+country+" = "+putcommas(newcases)]
        print("\n    "+"\n    ".join(printable))  
    except:
        print("Invalid country name or Weak Internet connection.")

def find_definition(user_input):
    with open(fullpath,"r") as JsonFile:
        data = json.load(JsonFile)
    array = user_input.split()
    if len(array) == 1:
        print("Invalid Arugment. Enter a word as an argument.")
        print("\n    "+"\n    ".join(data["help"]["specific_help"]["find_definition"]))
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


