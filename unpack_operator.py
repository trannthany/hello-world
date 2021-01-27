def func(x):
    def func2():
        print(x)
    
    return func2

print(func(3))

func(3)()

# func2 return None
print(func(2)())

#we can store function inside a variable
x = func(100)
x()


#unpacking operator
x = [1, 2, 3, 4, 5]
print(x) #this will print out the list
print(*x) #this will print out each value in the list or tuple, this is called unpacking

def func_3(x, y):
    print(x, y)

pairs = [(1,2), (3,4)]
func_3(*pairs)

for pair in pairs:
    func_3(*pair)
#this is the same as
for p in pairs:
    func_3(p[0], p[1])
    #however, this is not the python way

# We can also unpack dictionary
func_3(**{'x':2, 'y':5})
# Order does not matter
func_3(**{'y':5, 'x':2})


# *args and **kwargs
def func_2(*args, **kwargs):
    print(args, kwargs)
    print(*args) # we can unpack a list and pass it to a print statement
    #print(**kwargs) # we cannot unpack a dictionary and pass it to a print statement


# the *args is unpacking list or tuple
# the **kwargs is upacking dictionary

func_2(1,2,3,4,5, one=1, two=2)