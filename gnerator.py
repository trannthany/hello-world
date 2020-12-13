# def my_func():
#     n = 1
#     print('------------------------', n)
#     yield n
#     n += 1
#     print('------------------------', n)
#     yield n
#     n += 1
#     print('------------------------', n)
#     yield n

# def my_func():
#     for i in range(5):
#         print('------------------------', i)   
#         yield i



# # return vs yield (return stops the function, yield remembers the state of the function)

# x = my_func() # my_func() returns an iterator object

# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# #print(next(x)) # throw an error

#it is easier, we don need implement constructor, iter and next classes and raise exception
def list_iterator(list):
    for i in list:
        yield i

a = [1, 2, 3, 4, 5, 6]
mylist = list_iterator(a)

# print(next(mylist))
# print(next(mylist))
# print(next(mylist))
# print(next(mylist))
# print(next(mylist))
# print(next(mylist))
#print(next(mylist)) #throw an exception

for x in mylist:
    print(x)


