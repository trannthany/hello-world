# def decorator_func(func):
#     def wrapper_func():
#         print('X' * 20)
#         func()
#         print('Y' * 20)
#     return wrapper_func #the statement make this scope of code a closure

# @decorator_func #apply the decorator, which will allow us to skip the 2 lines below
# def say_hello():
#     print('Hello World')

# #hello = decorator_func(say_hello) # the hello will contain the inner-function
# #hello()

# say_hello()

def decorator_X(func):
    def wrapper_func():
        print('X' * 20)
        func()
        print('X' * 20)
    return wrapper_func #the statement make this scope of code a closure

def decorator_Y(func):
    def wrapper_func():
        print('Y' * 20)
        func()
        print('Y' * 20)
    return wrapper_func #the statement make this scope of code a closure

@decorator_X
@decorator_Y #apply the decorator, which will allow us to skip the 2 lines below
def say_hello():
    print('Hello World')

#hello = decorator_Y(decorator_X(say_hello)) # if we don't use @decorator_X and @decorator_Y
#hello()

say_hello()

def decorator_divide(func):
    def wrapper_func(a, b):
        print('divide', a, ' and ', b)
        if b == 0:
            print('division with zero is not allowed')
            return
        return a/b
    return wrapper_func

@decorator_divide
def divide(x, y):
    return x / y

print(divide(15, 5))