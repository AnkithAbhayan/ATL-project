import json
from misc import functions
from functions import *
print("Hi, I am a chat bot .You can ask me anything but I'm not sure I can answer all questions")
print("enter 'help' for all commands")
print("enter 'stop' to stop")

function_caller = {
    "add numbers":addition,
    "subtract numbers":subtraction,
    "divide numbers":division,
    "multiply numbers":multiplication,
    "find definition":find_definition
}
tdata = load_database()
functions = ["add numbers","subtract numbers","divide numbers","multiply numbers"]
while True:
    user_question = input("ask me anything:")
    if user_question == "help":
        print(functions)
    elif user_question == "stop":
        print("thankyou for your time")
        break
    elif function_caller.get(user_question):
        function_caller.get(user_question)()
    elif tdata.get(user_question):
        print("another user entered this answer:")
        print(tdata.get(user_question))
        prompt = input("is this correct?:")
        if prompt == "yes":
            print("ok thankyou")
        else:
            answer = input("your answer:")
            print("ok thankyou")
        tdata[user_question] = answer
    else:
        array = user_question.split()
        if array[0:2] == ["total","cases"]:
            country = array[2]
            r = requests.get("https://api.covid19api.com/dayone/country/"+country+"/status/confirmed")
            data = json.loads(r.text)
            print("total cases in "+country+" = "+putcommas(str(data[-1]["Cases"])))
        elif array[0:2] == ["new","cases"]:
            country = array[2]
            r = requests.get("https://api.covid19api.com/dayone/country/"+country+"/status/confirmed")
            data = json.loads(r.text)
            print("new cases (daily) in "+country+" = "+putcommad(str(data[-1]["Cases"]-data[-2]["Cases"])))   
        else:
            print("I don't know the answer")
            print("do you know the answer? if yes - please enter the answer. or enter 'sorry'")
            answer = input("your answer:")
            if answer == "sorry":
                print("ok,that's alright")
            else:
                print("thank you so much for the answer")
                tdata.update({user_question:answer})
    print()
save_database(tdata)