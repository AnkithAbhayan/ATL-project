from src import functions,misc,usermod
import pathlib

misc.introduction()
user = usermod.authenticate()
command_palette = {
    "help":misc.help_info,
    "stop":misc.stop,
    "find_definition":functions.find_definition,
    "total_cases":functions.total_cases,
    "new_cases":functions.new_cases,
    "credits":misc.credits,
    "usermod":usermod.parse
}

while True:
    user_question = input(f"{user}$ ")
    if command_palette.get(user_question.split()[0]):
        command_palette[user_question.split()[0]](user_question)  
    elif command_palette.get(" ".join(user_question.split()[0:2])):
    	command_palette[" ".join(user_question.split()[0:2])](user_question)
    else:
        print("You entered an unknown command. Enter 'help' for more info")
    print()