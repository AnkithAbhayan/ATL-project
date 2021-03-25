from src import functions,misc,usermod
import pathlib

command_palette = {
    "help":misc.help_info,
    "stop":misc.stop,
    "find_definition":functions.find_definition,
    "total_cases":functions.total_cases,
    "new_cases":functions.new_cases,
    "credits":misc.credits,
    "usermod":usermod.parse
}

misc.introduction()
user = usermod.authenticate()

while True:
    user = usermod.authenticate()
    user_question = input(f"{user}$ ")
    if misc.parse(user_question,command_palette):
        print()
        continue
    if command_palette.get(user_question.split()[0]):
        command_palette[user_question.split()[0]](user_question)  
    else:
        print("You entered an unknown command. Enter 'help' for more info")
    print()