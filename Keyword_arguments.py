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
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
        print('----')

cheeseshop("Shrubberry", "It's very bushy, sir.",
           "It's really very, VERY bushy, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Bush Shop Sketch")