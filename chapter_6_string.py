# if we don't want characters prefaced by \ to be interpreted as special characters, we can use raw strings by adding an r before the first quote:

print(r'C:\some\name')
print('C:\some\name')

word = 'Python'
print(word[2:5]) # characters from position 2 to 5 (excluded 5)
print(word[:5]) # is the same as word[0:5]

# [] means list
squares = [1, 3, 9, 16, 25]
print(squares)

#slicing returns a new list
new_list = squares[-3:]
print(new_list)

#list supports concatenation
print(squares + new_list)
longer_list = squares + new_list
print(longer_list)

print("List of lists")
#list of list
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][0])
print(x[1][2])