#function is storing and reusing steps

def thing():
    print('Hello')
    print('Fun')

#function with an argument
def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')

#function that returns a value
def say_hello():
    return "Hello"

#the actual function takes inputs and return an output
def sum_two_nums(n1, n2):
    return n1 + n2

#invoking/calling functions
thing()
print('Zip')
thing()

big = max('Hello world')
tiny = min('Hello world')

print(big) #the biggest is the w
print(tiny) #the smalles is the blank

greet('en')
greet('es')
greet('fr')

print(say_hello(), "Thany")

print(sum_two_nums(5, 10))

sum = sum_two_nums(25, 26)
print(sum)