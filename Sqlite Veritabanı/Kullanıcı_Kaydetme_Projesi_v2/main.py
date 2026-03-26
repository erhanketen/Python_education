import funcs_for_main
from funcs_for_main import current_user_id

print(funcs_for_main.Fore.LIGHTWHITE_EX+"""
-----------------------------------------

        USER REGISTRATION PROGRAM
      
-----------------------------------------
""")

while True:
    print(funcs_for_main.Fore.LIGHTWHITE_EX+"""    
Functions:

1- Register
2- Login
3- Quit Program
    """)
    user_input = input("Chose an option:")
    if user_input == "1":
        try:
            register = funcs_for_main.register()
        except:
            print(funcs_for_main.Fore.RED+"Something went wrong")
            break
    elif user_input == "2":
        try:
            while True:
                login = funcs_for_main.login()
                user = funcs_for_main.user_page(login)
                break
        except:
            print(funcs_for_main.Fore.RED + "Something went wrong")
            break
        finally:
            funcs_for_main.logout_connection(user)
    elif user_input == "3":
        print(funcs_for_main.Fore.LIGHTWHITE_EX+"Program shutting down")
        funcs_for_main.sleep(1.5)
        break
    else:
        print(funcs_for_main.Fore.RED+"Invalid Input")






