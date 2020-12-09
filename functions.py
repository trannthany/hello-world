#function a group of statements that perform a specific task

#built-in function e.g. print(), input(), min() ...

#user defined funtion

#def nameofyourfunction(arg1, arg2, arg3, ...):
    #statements 
    #statements can be the built-function or your defined functions

def sum(arg1, arg2):
    if type(arg1) != type(arg2):
        print("Please give the args of same type")
        return #this return nothing and anything after the return will not be executed
    print(arg1 + arg2)

def sum_that_return_value(arg1, arg2):
    if type(arg1) != type(arg2):
        print("Please give the args of same type")
        return #this return nothing and anything after the return will not be executed
    return(arg1 + arg2)
#call your defined function
sum(15, 50)
sum("Hello", " World")
sum(15.7, 80.253)
sum("hello", 23)

a = sum_that_return_value(23, 31)
print(a)