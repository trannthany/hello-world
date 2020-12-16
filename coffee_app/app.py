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

    # the := means the user_input variable gets the value from input function
    while(user_input := input(MENU_PROMT)) != "5":
        print(user_input)

menu()
