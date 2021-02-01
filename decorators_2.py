# Decorators provide a way to modify functions using other functions
# This is ideal when you need to extend the functionality of functions that you don't want to modify

# def decor(func):
#     def wrap():
#         print("=" * 11)
#         func()
#         print("=" * 11)
#     return wrap()


# def print_text():
#     print("Hello world!")

# decorated = decor(print_text)

#decorated()

###############################################################
# this is the same as the code above
def decor(func):
    def wrap():
        print("=" * 11)
        func()
        print("=" * 11)
    return wrap()
# we define a function that we can "decorate" it with the @ symbol
# 
@decor
def print_text():
    print("Hello world!")