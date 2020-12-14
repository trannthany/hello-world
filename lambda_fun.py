# #function 1
# def double(x):
#     return x * 2
# #function 2
# def add(x, y):
#     return x + y
# #function 3
# def product(x, y, z):
#     return x * y * z




double = lambda x : x * 2 # this is the same as the functoin 1
add = lambda x, y : x + y #
product = lambda x, y, z : x * y * z

print(double(5))
print(add(10, 20))
print(product(7,3,2))

#WHy do we use lambda function?
#lambda takes functions as argument but it can also return a function

#map function
my_list = [2, 5, 8, 10, 9 ,3]

a = map(lambda x : x * 2, my_list)
print(a)
print(list(a))#convert the map object to the list
#we can see that the lambda function double values in my list

#let make it more complext
my_list2 = [1,1,2,3,5,8,13]
my_list3 = [1,4,7,8,5,1,12]

b = map(lambda x, y: x + y, my_list2, my_list3 )
print(b)
print(list(b))

#filter function
c =filter(lambda x : x%2==0, my_list)
print(c)
print(list(c))

d = filter(lambda x: True if x > 5 else False, my_list2)
print(list(d))

#reduce function, this function requires functools module (from functools import reduce)
from functools import reduce
e = reduce(lambda x, y : x + y, my_list3) # sum values in the list, e store the sum value
print(e)