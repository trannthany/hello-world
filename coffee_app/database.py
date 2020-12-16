# CREATE TABLE IF NOT EXISTS beans (id INTEGER PRIMARY KEY, name TEXT, method TEXT, rating INTEGER);
# INSERT INTO beans VALUES (1, 'Exlusive Blend', 'Percolator', 65); #id is auto increment, this is redundant
# INSERT INOT beans (name, method, rating) VALUES ('Exclusive Blend', 'Percolator', 65);
# SELECT * FROM beans; # * means all the columns
# SELECT name, method, rating FROM beans;
# SELECT name, method, rating FROM beans ORDER BY rating DESC;
# SELECT method, rating FROM beans ORDER BY rating DESC LIMIT 1; # LIMIT 1 means we only get one row back (the top one)
# SELECT * FROM beans WHERE name = 'Exclusive Blend';
"""
    SELECT * FROM beans
    WHERE name = 'Exclusive Blend'
    ORDER BY rating DESC
    LIMIT 1;
"""

"""
    SELECT method FROM beans GROUP BY method;
"""
#aggregate method/function e.g. AVG(rating)
""" 
    SELECT method, AVG(rating) FROM beans GROUP BY method;
"""


import sqlite3

#Quary
CREATE_BEANS_TABLE = "CREATE TABLE IF NOT EXISTS beans (id INTEGER PRIMARY KEY, name TEXT, method TEXT, rating INTEGER);"
INSERT_BEAN = "INSERT INTO beans(name, method, rating) VALUES(?, ?, ?);" #the question marks take the inputs as a tuple
GET_ALL_BEANS = "SELECT * FROM beans;"
GET_BEANS_BY_NAME = "SELECT * FROM beans WHERE name = ?;"
GET_BEST_PREPARATION_FOR_BEAN = """
SELECT * FROM beans
WHERE name = ?
ORDER BY rating DESC
LIMIT 1;"""


#create a database and create a connection object
def connect():
    return sqlite3.connect("coffee_app/data.db")# if is not exited, then the sqlite3 will create it

def create_tables(connection):
    #make the connection and execute the query
    with connection:
        connection.execute(CREATE_BEANS_TABLE)

def add_bean(connection, name, method, rating):
    with connection:
        return connection.execute(INSERT_BEAN, (name, method, rating)).fetchall()

def get_all_beans(connection):
    with connection:
        return connection.execute(GET_ALL_BEANS).fetchall() #we have pass a tuple (name, ), fetchall() return every rows

def get_best_preparation_for_beans(connection, name):
    with connection:
        return connection.execute(GET_BEST_PREPARATION_FOR_BEAN, (name,)).fetchone()#we one just one row

def get_beans_by_name(connection, name):
    with connection:
        return connection.execute(GET_BEANS_BY_NAME, (name,)).fetchall()

