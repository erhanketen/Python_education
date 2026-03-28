import DB
from DB import invalid_email
from random import randint
from time import sleep
from colorama import Fore , init
init(autoreset=True)


def connector(func):
    def wrapper(obj,*args,**kwargs):
        try:
            obj.make_connection()
            result = func(obj,*args,**kwargs)
            return result
        finally:
            obj.cut_connection()
    return wrapper

@connector
def generate_user_id(identification):
    while True:
        num ="user_"+str(randint(100_000_000,999_999_999))
        if identification.is_user_id_unique(num):
            return num

@connector
def generate_log_id(indentification):
    while True:
        log = "log_"+str(randint(100_000_000,999_999_999))
        if indentification.is_log_id_unique(log):
            return log

def register():
    identification = DB.User()
    user_id = generate_user_id(identification)
    log_id = generate_log_id(identification)
    del identification

    name = input( "Name:")
    try:
        age = int(input( "Age:"))
    except ValueError:
        print(Fore.RED+"Invalid Age")
        return False
    email = input("Email:")
    password = input("Password:")

    new_user = DB.User(name=name, age=age, user_id=user_id, email=email, password=password)

    print(Fore.LIGHTWHITE_EX + "Registering...")
    conn = register_connection(new_user)
    if not conn:
        return False
    else:
        sleep(1.5)
        print(Fore.LIGHTGREEN_EX + "Registration Complete")
        insert_log_connection(new_user,(log_id,user_id,"REGISTERED"))
        return conn

@connector
def register_connection(add_user):

    register_obj = add_user.register_user()
    if register_obj == "UsedEmailError":
        print(Fore.RED + "There is already a user with that email")
        return False
    elif register_obj == "InvalidEmailError":
        print(Fore.RED + "Invalid Email")
        return False
    elif not register_obj:
        print(Fore.RED+"Something went wrong")
        return False
    else:
        return True

def login():
    email = input("Email:")
    password = input("Password:")

    user = DB.User(email=email, password=password)
    log_id = generate_log_id(user)
    print(Fore.LIGHTWHITE_EX + "Logging in...")
    conn = logging_connection(user)
    if not conn:
        return False
    else:
        sleep(1.5)
        print(Fore.LIGHTGREEN_EX + "Login Successful")
        insert_log_connection(user,(log_id,conn[0][3],"LOGGED_IN"))
        return conn

@connector
def logging_connection(_user_):
    user_info = _user_.login_user()
    if user_info == "UnSuccessfulLoginError":
        print(Fore.RED+"Email or Password is Incorrect")
        return False
    return user_info

@connector
def update_connection(user_obj,user_info):
    print(Fore.LIGHTWHITE_EX + "Updating...")
    sleep(1.5)
    user_obj.update_user(user_info)
    print(Fore.LIGHTGREEN_EX + "Updating Successful")

@connector
def delete_connection(user_obj):
    print(Fore.LIGHTWHITE_EX+"Deleting...")
    sleep(1.5)
    user_obj.delete_user()
    print(Fore.LIGHTGREEN_EX + "Deleting Successful")

@connector
def logout_connection(user_obj,user_id):
    if user_obj.get_state():
        print(Fore.LIGHTWHITE_EX + "Logging Out...")
        sleep(1.5)
        user_obj.logout_user()
        log_id = generate_log_id(user_obj)
        insert_log_connection(user_obj,(log_id,user_id,"LOGGED_OUT"))

@connector
def insert_log_connection(obj,user_info):
    obj.insert_log(user_info)

@connector
def show_connection(user_obj):
    return user_obj.show_user_info()

current_user_id = list()

def user_page(user_info):
    print(Fore.LIGHTWHITE_EX+"""
-------------------------------

           WELCOME

-------------------------------
    """)

    global current_user_id
    current_user_id.append(user_info[0][3])
    user = DB.User(user_id=current_user_id[0])

    while True:
        print(Fore.LIGHTWHITE_EX+"""
Actions:

1- See Account Information
2- Update Account Information
3- Delete Account
4- Log Out       
        """)
        user_input = input("Choose an action:")

        if user_input == "1":
            log_id = generate_log_id(user)
            print(Fore.LIGHTBLUE_EX+show_connection(user))
            insert_log_connection(user,(log_id,user.user_id,"USER_INFO_SHOWED"))
        elif user_input == "2":
            log_id = generate_log_id(user)
            name = input("Name:")
            while True:
                try:
                    age = int(input("Age:"))
                    break
                except ValueError:
                    print(Fore.RED+"Invalid Age")
            while True:
                email = input("Email:")
                if not invalid_email(email):
                    print(Fore.RED + "Invalid Email")
                    continue
                else:
                    break
            password = input("Password:")

            new_user_info = (name, age, email, password)

            update_connection(user,new_user_info)
            insert_log_connection(user,(log_id,user.user_id,"USER_UPDATED"))

        elif user_input == "3":
            log_id = generate_log_id(user)
            insert_log_connection(user,(log_id,user.user_id,"USER_DELETED"))
            delete_connection(user)
            return user

        elif user_input == "4":
            return user
        else:
            print(Fore.RED+"Invalid Input")

