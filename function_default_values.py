def ask_ok(promp, retries=4, reminder='Please try again!'):
    while True:
        ok = input(promp)
        if ok in ('y', 'ye', 'yes'):
            return True
        
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        
        retries = retries - 1

        if retries < 0:
            raise ValueError('invalid user response')

        print(reminder)

# The function above can be called in several ways:

#     giving only the mandatory argument: ask_ok('Do you really want to quit?')

#     giving one of the optional arguments: ask_ok('OK to overwrite the file?', 2)

#     or even giving all arguments: ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')


# The default values are evaluated at the point of function definition in the defining scope, so that
i = 5

def f(arg=i):
    print(arg)

i = 6
f() # this will print 5

# Warning *****
# The function's default values only evaluate once

def fa(a, L=[]):
    L.append(a)
    return L

print(fa(1))
print(fa(2))
print(fa(3))

print('-----------')

# If you don’t want the default to be shared between subsequent calls, you can write the function like this instead:
def fb(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(fb(1))
print(fb(2))
print(fb(3))



