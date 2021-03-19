from functions import *
introduction()

function_caller = {
    "help":help_info,
    "stop":stop,
    "find_definition":find_definition,
    "total_cases":total_cases,
    "new_cases":new_cases,
    "credits":credits
}
while True:
    user_question = input("ChatBot$ ")
    if function_caller.get(user_question.split()[0]):
        function_caller[user_question.split()[0]](user_question)  
    elif function_caller.get(" ".join(user_question.split()[0:2])):
    	function_caller[" ".join(user_question.split()[0:2])](user_question)
    else:
        print("You entered an unknown command. Enter 'help' for more info")
    print()
