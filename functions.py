import json
import os
import sys
import requests
def addition():
    first_number = int(input("enter first number:"))
    second_number = int(input("enter second number:"))
    answer = first_number+second_number
    print("the sum is :"+str(answer))
def subtraction():
    first_number = int(input("enter first number:"))
    second_number = int(input("enter second number:"))
    answer = first_number-second_number
    print("the difference is :"+str(answer))
def division():
    first_number = int(input("enter divident:"))
    second_number = int(input("enter divisor number:"))
    answer = first_number/second_number
    print("the answer is :"+str(answer))
def multiplication():
    first_number = int(input("enter first number:"))
    second_number = int(input("enter second number:"))
    answer = first_number*second_number
    print("the product is :"+str(answer))
def load_database():
    path = find_database_path()
    if os.path.exists(path) == False:
        with open(path,"w") as Jsonfile:
            json.dump({"tdata":{}},Jsonfile,indent=4)
    with open(path,"r") as Jsonfile:
        data = json.load(Jsonfile)
    tdata = data["tdata"]
    with open(path,"w") as Jsonfile:
        json.dump(data,Jsonfile,indent=4)
    return tdata
def save_database(tdata):
    path = find_database_path()
    data = {"tdata":tdata}
    with open(path,"w") as Jsonfile:
        json.dump(data,Jsonfile,indent=4)
def find_database_path():
    relative_path = sys.argv[0]
    letter_list = [x for x in relative_path]
    slashindex = []
    lix = ["\ "]   
    if lix[0][0] not in letter_list:
        return "database.json"
    else:
        for item in letter_list:
            if item == lix[0][0]:
                indexx = letter_list.index(lix[0][0])
                slashindex.append(indexx)
                letter_list[indexx] = "a"
        return relative_path[0:slashindex[-1]]+"\database.json"
def find_definition():
    name = input("enter the word you want to find the definition of:")
    try:
        response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/"+name)
        data = json.loads(response.text)
    except:
        print("internet error")
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