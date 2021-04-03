import json
from src.usermod_funcs.account_class import account
def login(safety,jsonpath):
    name = input("Enter username:")
    my_account = account(username=name,fullpath=jsonpath)
    if my_account.is_username_existing():
        my_account.set_password(input(f"Enter password for user '{my_account.username}': "))
        if my_account.is_correct_password():
            my_account.login()
            print(f"Successfully logged in as '{my_account.username}'.")
        else:
            print("Wrong password!")
            return ""
    else:
        print(f"The username '{my_account.username}' doesnt exist. Try making a new one by using 'usermod -n'")
        return
    return my_account.username