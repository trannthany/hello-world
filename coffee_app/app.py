# Python SQLite Tutorial: Build a Python project with a SQLite database
# https://www.youtube.com/watch?v=iXYeb2artTE

#

import database as my_db

MENU_PROMT = """-- Coffee Bean App --

Please choose one of these options:

1) Add a new bean.
2) See all beans.
3) Find a bean by name.
4) See which preparation method is best for a bean.
5) Exit.

Your selection:"""


def menu():
    connection = my_db.connect()
    my_db.create_tables(connection)

    # the := means the user_input variable gets the value from the input function, and the operation (:=) keeps the loop running until user put 5
    while(user_input := input(MENU_PROMT)) != "5":
        if user_input == "1":
            name = input("Enter bean name: ")
            method = input("Enter how you've prepared it: ")
            rating = int(input("Enter your rating score (0-100): "))
            
            my_db.add_bean(connection, name, method, rating)
        elif user_input == "2":
            beans = my_db.get_all_beans(connection)

            for bean in beans:
                print(bean)
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            print("Invalid input please try again!!")

menu()
