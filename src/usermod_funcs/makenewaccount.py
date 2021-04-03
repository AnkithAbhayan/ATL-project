import json
from src.usermod_funcs.account_class import account
def makenewaccount(safety,jsonpath):
    my_account = account(username=input("enter username: "),fullpath=jsonpath)
    if my_account.is_username_existing():
        print("Username already taken.")
        return ""
    password = my_account.keep_asking_for_input("Enter Password: ")
    my_account.set_password(password)
    my_account.register_account()
    my_account.login()
    print("Successfully made a new account.")
    return my_account.username