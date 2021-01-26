# Dictionaries are data structures used to map arbitary keys to values
# List can be thought of as dictionaries with integer keys within a certain range
# Dictionaries can be indexed in the same way as lists, using square brackets containing keys

# dictionary is represented by a key:value pair
ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])

# Index a key that isn't part of the dictionary returns a KeyError
primary = {"red":[255,0,0], "green":[0,255,0], "blue":[0,0,255]}
print(primary["red"])
#print(primary["yellow"])

# an empty dictionary is defined as {}

# Only immutable objects can be used as keys to dictionaries
this_is_dict = {1:"Cat", 2:"Dog"}
print(this_is_dict[1])

this_is_also_dict = {"one two three":[1,2,3]}
print(this_is_also_dict["one two three"])

#this_is_not_dict = {[1,2,3]:"one two three"}
how_about_this_one = {2: 4, 3:9, 4:16}
print(how_about_this_one[4])

# dictionary keys can be assigned to different values
this_is_dict[3] = "Hamster"
this_is_dict[4] = "Gold Fish"
print(this_is_dict)


# To determine whether a key is in a dictionary, you can use in and not in 
print(1 in this_is_dict)
print(6 in this_is_dict)
print(8 not in this_is_dict)

# get method returns a specific value ('None' is by default) if the key is not found
# the indexing returns traceback
#print(this_is_dict[6])
print(this_is_dict.get(6))
print(this_is_dict.get(10, "10 is not in dictionary"))

fib = {1:1, 2:1, 3:2, 4:3}
print(fib.get(7,5))
print(fib.get(4,0))