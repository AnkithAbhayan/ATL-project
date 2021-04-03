import json
from src.usermod_funcs.account_class import account
def changename(safety,jsonpath):
    my_account = account(fullpath=jsonpath)
    my_account.set_username(my_account.json_data["current_user"])
    print(f"Changing name of user '{my_account.username}'. Not the user you wanted? Login with another user using 'usermod -l'.")
    my_account.set_password(input("Enter password: "))
    if not my_account.is_correct_password():
        print("Wrong password.")
        return
    new_name = my_account.keep_asking_for_input("Enter new username: ")
    my_account.set_username(new_name)
    if my_account.is_username_existing():
        print("Username Already exists.")
        return
    my_account.change_username_to(my_account.username)
    print(f"Successfully changed username to '{my_account.username}'")