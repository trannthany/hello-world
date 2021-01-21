# **name_of_argument - the ** implies that the argument takes a dictionary
# *name_of_arguement - the * implies that the argument takes a tuple

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("---------------------------------------")
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")    

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

def cheeseshop(kind, *arguments, **keywords):
    print("---------------------------------------")
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
        print('--')
    print("-" * 40) # print 40 dashes '-'
    for kw in keywords:
        print(kw, ":", keywords[kw])
        print('----')

cheeseshop("Shrubberry", "It's very bushy, sir.",
           "It's really very, VERY bushy, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Bush Shop Sketch")

# this function takes positional or keyword
def standard_arg(arg):
    print(arg)

def standard_arg(arg, /):
    print(arg)

def standard_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

#both callings work
standard_arg(2)
standard_arg(arg=2)

pos_only_arg(1)
#pos_only_arg(arg=1) # this will give a traceback

#kwd_only_arg(3) # this will give a traceback
kwd_only_arg(arg=3)

combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)

# As guidance:

#     Use positional-only if you want the name of the parameters to not be available to the user. This is useful when parameter names have no real meaning, if you want to enforce the order of the arguments when the function is called or if you need to take some positional parameters and arbitrary keywords.

#     Use keyword-only when names have meaning and the function definition is more understandable by being explicit with names or you want to prevent users relying on the position of the argument being passed.

#     For an API, use positional-only to prevent breaking API changes if the parameter’s name is modified in the future.

# https://docs.python.org/3.8/tutorial/controlflow.html

