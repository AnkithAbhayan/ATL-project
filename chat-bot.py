import json
from functions import *
print("Hi, I am a chat bot .You can ask me anything but I'm not sure I can answer all questions")
print("enter 'help' for all commands")
print("enter 'stop' to stop")
function_caller = {
    "add numbers":addition,
    "subtract numbers":subtraction,
    "divide numbers":division,
    "multiply numbers":multiplication
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
        print("I don't know the answer")
        print("do you know the answer? if yes - please enter the answer. or enter 'sorry'")
        answer = input("your answer:")
        print("thankyou so much for the answer")
        tdata.update({user_question:answer})
        print(tdata)
    print()
save_database(tdata)