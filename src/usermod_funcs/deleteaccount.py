import json
from src.usermod_funcs.account_class import account
def deleteaccount(safety,jsonpath):
    my_account = account(fullpath=jsonpath)
    my_account.set_username(my_account.json_data["current_user"])
    print(f"Deleting account of user '{my_account.username}'. Not the user you wanted? Login with another user using 'usermod -l'")
    my_account.set_password(input("Enter password: "))
    if not my_account.is_correct_password():
        print("Wrong password")
        return
    my_account.delete_account()
    print("Successfully deleted account.")