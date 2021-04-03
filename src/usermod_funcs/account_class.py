import json
class account:
    def __init__(self,username="",password="",fullpath=""):
        self.username = username
        self.password = password
        self.fullpath = fullpath
        with open(fullpath,"r") as JsonFile:
            data = json.load(JsonFile)
        self.json_data = data

    def is_correct_password(self):
        if self.json_data["users"][self.username]["password"] == self.password:
            return True
        return False

    def is_username_existing(self):
        if self.json_data["users"].get(self.username):
            return True
        return False

    def set_password(self,password):
        self.password = password

    def set_username(self,username):
        self.username = username

    def keep_asking_for_input(self,prompt):
        while True:
            user_input = input(prompt)
            if user_input:
                return user_input
            else:
                print("Not valid input. (its empty)")

    def register_account(self):
        self.json_data["users"].update({self.username:{"password":self.password}})
        with open(self.fullpath,"w") as JsonFile:
            json.dump(self.json_data,JsonFile,indent=4)

    def delete_account(self):
        del self.json_data["users"][self.username]
        self.json_data["current_user"] = ""
        with open(self.fullpath,"w") as JsonFile:
            json.dump(self.json_data,JsonFile,indent=4)

    def login(self):
        self.json_data["current_user"] = self.username
        with open(self.fullpath,"w") as JsonFile:
            json.dump(self.json_data,JsonFile,indent=4)

    def change_password_to(self,password):
        self.password = password
        self.json_data["users"][self.username]["password"] = self.password
        with open(self.fullpath,"w") as JsonFile:
            json.dump(self.json_data,JsonFile,indent=4)

    def change_username_to(self,username):
        oldname = self.json_data["current_user"]
        self.username = username
        new_data = {self.username:{"password":self.json_data["users"][oldname]["password"]}}
        del self.json_data["users"][oldname]
        self.json_data["users"].update(new_data)
        self.json_data["current_user"] = self.username
        with open(self.fullpath,"w") as JsonFile:
            json.dump(self.json_data,JsonFile,indent=4)