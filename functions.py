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
        #print("Please give the args of same type")
        return #this return nothing and anything after the return will not be executed
    return(arg1 + arg2)

def student(name="Unkown name", age=0): #default value
    print("name: ", name)
    print("age:", age)

def showlist_of_marks(*marks): #this means we can provide multiple arguments
    print('Marks', marks)



def show_key_value_pair_argument(**marks):
    for key, value in marks.items():
        print(key, " ", value)

#calling your defined functions
sum(15, 50)
sum("Hello", " World")
sum(15.7, 80.253)
sum("hello", 23)

a = sum_that_return_value(23, 31)
print(a)
print(sum_that_return_value(23, "hello"))

student()
student('Tom')

showlist_of_marks(1, 4, 5, 6, 7)
show_key_value_pair_argument(English=95, Math=70, Physics=80)