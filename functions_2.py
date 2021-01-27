def func(x, y):
    print('Run', x, y)
    return x * y, x + y
# the func will return a tuple

print(func(5, 6))

# we can a function in a function

def func_1(x, y):
    print("Run")
    def func_2(z, a, k):
        print("Jump")
    
    func_2(1, 2, 3)

func_1(1, 2)

#function default value

def func_3(x, y=None):
    return "nothing", x, y

print(func_3(3))

print(func_3(3,4))