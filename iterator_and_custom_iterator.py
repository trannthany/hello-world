# iterator has 2 special methods
# __iter__() gets an iterator
# __next__() 

# a = [1, 2, 3, 4, 5, 9, 7]

# my_iterator = iter(a)

# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))#this will give an excption


# create custom iterator class
# an iterator always has __iter__() and __next__()

class ListIterator:
    def __init__(self, a_list):
        self.__list = a_list
        self.__index = -1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.__index += 1
        if self.__index >= len(self.__list):
            raise StopIteration
        return self.__list[self.__index]
a = [1, 2, 3, 4, 5, 9, 7]
mylist_iterator = ListIterator(a)
not_my_iterator = iter(mylist_iterator)

# print(next(mylist_iterator))
# print(next(mylist_iterator))
# print(next(mylist_iterator))
# print(next(mylist_iterator))
# print(next(mylist_iterator))
# print(next(mylist_iterator))
# print(next(mylist_iterator))
# print(next(mylist_iterator))

for i in not_my_iterator:
    print(i)