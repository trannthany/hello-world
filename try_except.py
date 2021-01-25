# a try statement can have multiple different except blocks to handle different exceptions
# multiple exceptions can also be put into single except block using parentheses, to have except block handle all of them

# variable = input("Enter a number: ")
# try:
#     number = int(variable)
#     print(variable + " Hello")
#     print(number/2)
    
#     print(number + " Hello")
#     #print(6/number)
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except (ValueError, TypeError):
#     print("An error occurs")


# An except statement without any exception specified will catch all errors
# However, it is not adviced to except without any specific exception

try:
    word = "spam"
    print(word/0)
except:
    print("Something is wrong")


# finally ensures code runs no matter what errors occur
# finally is placed at the buttom of a try/except

try:
    print(1)
    print( 10 / 0)
except ZeroDivisionError as err:
    print(err)
    print("I should write my own custom error so that to show that I understand why error occurs")
finally:
    print("This is executed last, no matter what ...")