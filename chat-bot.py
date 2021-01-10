import json
from functions import *
import sys
print("Hi, I am a chat bot .You can ask me anything but I'm not sure I can answer all questions")
print("enter 'help' for all commands")
print("enter 'stop' to stop")
function_caller = {
    "add numbers":addition,
    "subtract numbers":subtraction,
    "divide numbers":division,
    "multiply numbers":multiplication
}
functions = ["add numbers","subtract numbers","divide numbers","multiply numbers"]
while True:
    user_question = input("ask me anything:")
    if user_question == "help":
        print(functions)
    elif user_question == "stop":
        print("thankyou for your time")
        sys.exit()
    elif function_caller.get(user_question):
        function_caller.get(user_question)()
    else:
        print("I don't know the answer")
    print()