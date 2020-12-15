# def outerFunction(text):
#     def innerFunction():
#         print(text)
#     innerFunction()

# outerFunction("Hello")

# def pop(list):
#     def get_last_item(my_list):
#         return my_list[len(list) - 1]
    
#     list.remove(get_last_item(list))
#     return list


# a = [1, 2, 3, 4, 5, 6]
# print(pop(a))
# print(pop(a))
# print(pop(a))

### Closure - is a function that depends on one or more variables which are declared outside the function
def outerFunction(text):
    def innerFunction(): #the innerFunction depends on the text variable which is outside its function therefore, the innerFunction() is a closure
        print(text)
    return innerFunction #return the the inner function without the parentasis ()

a = outerFunction("Hello")
# a ('asdfdsf')
# print(a())
a() #just calling the innerFunction(), the innerFunction saves the value

def nth_power(exponent):
    def pow_of(base):
        return pow(base, exponent)
    return pow_of

square = nth_power(2) 
print(square(3)) #the square stores the return value which is the pow_of (inner function)

cube = nth_power(3)
print(cube(2))