result = None

a = float(input('Number 1: '))
b = float(input('Number 2: '))

# try:
#     result = a / b
# except:
#     print("I know the kind of error, so I write this error message")

# try:
#     result = a / b
# except Exception as e:
#     print("Error = ", e) # the exception is a generic exception, if we use type(e) it will show us the specific type of error, but it is not a good practice

try:
    result = a / b
except ZeroDivisionError as e:
    print("Error = ", e) # The ZeroDivisionErrror only catch ZeroDivisionError
except TypeError as e:
    print("Error = ", e) # this to catch TypeError, if we don't know which exception to catch, then we must keep testing and using Exception to find out the type(e)
else:
    print('__else__') # if code does not have any erro it will run this else statement
finally:
    print('__finally__') #this statement will run whether the code has error or not, this statement helps to make sure the open file/database is close if there is any error

try: #try and finally can be used without the except clause
    print(a/b)
finally:
    print("Something must be done if there is an exception")

print('Result = ', result)
print('End')