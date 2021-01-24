# Generators are type of iterable, like lists or tuples
# Generators don't allow indexing with arbitrary indeces, but they can still be iterated through with for loops
# Generators can be created using functions and the yield statement
# The yield statement is used to define a generator, replacing the return of a function to provide a result to its caller without destroying local varialbes
def countdown():
    i = 5
    while i > 0:
        yield i
        i -= 1

for a in countdown():
    print(a)

# Due to the fact that Generators yield one item at a time, they don't have the memory restrictions of lists
# In fact, Generators can be infinite!!!
# Note: Generators allow me to declare a function that behaves like an iterator, i.e. it can be used for a for loop

# def infinite_sevens():
#     while True:
#         yield 7

# for i in infinite_sevens():
#     print(i)

def is_prime(n: int) -> bool:
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# prime number generator
def get_primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

print(get_primes())

#Finite generators can be converted into lists by passing them as arguments to the list function
def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(numbers(11)))

def make_word():
    word = ""
    for ch in "spam":
        word += ch
        yield word

print(list(make_word()))