import json
from src.usermod_funcs.account_class import account
def changepassword(safety,jsonpath):
    my_account = account(fullpath=jsonpath)
    my_account.set_username(my_account.json_data["current_user"])
    print(f"Changing password of user '{my_account.username}'. Not the user you wanted? Login with another user using 'usermod -l'.")
    my_account.set_password(input("current password: "))
    if not my_account.is_correct_password():
        print("Wrong password.")
        return
    password = my_account.keep_asking_for_input("Enter new password: ")
    my_account.set_password(password)
    my_account.change_password_to(my_account.password)
    print("Successfully changed password.")