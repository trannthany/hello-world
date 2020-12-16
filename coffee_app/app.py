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

def print_each_bean(beans):
    for bean in beans:
        print(f"{bean[1]} ({bean[2]}) - {bean[3]}/100")

def prompt_add_new_bean(connection):
    name = input("Enter bean name: ")
    method = input("Enter how you've prepared it: ")
    rating = int(input("Enter your rating score (0-100): "))
            
    my_db.add_bean(connection, name, method, rating)


def prompt_see_all_beans(connection):
    beans = my_db.get_all_beans(connection)

    print_each_bean(beans)

def prompt_to_find_bean(connection):
    name = input("Enter bean name to find: ")
    beans = my_db.get_beans_by_name(connection, name)
    print_each_bean(beans)

def prompt_find_best_method(connection):
    name = input("Enter bean name to find: ")
    best_method = my_db.get_best_preparation_for_beans(connection, name)

    print(f"The best preparation for {name} is: {best_method[2]}") #the method is in the index 2 (column 3)
def menu():
    connection = my_db.connect()
    my_db.create_tables(connection)

    # the := means the user_input variable gets the value from the input function, and the operation (:=) keeps the loop running until user put 5
    while(user_input := input(MENU_PROMT)) != "5":
        if user_input == "1":
            prompt_add_new_bean(connection)
        elif user_input == "2":
            prompt_see_all_beans(connection)
        elif user_input == "3":
            prompt_to_find_bean(connection)
        elif user_input == "4":
            prompt_find_best_method(connection)
        else:
            print("Invalid input please try again!!")

menu()
