a, b = 0, 1
# a, b = 0, 1 is the same as:
# a = 0
# b = 1
while a < 10:
    print(a)
    a, b = b, a+b
# the a, b = b, a+b is the same as:
# a = b
# b = a + b


# the key word argument 'end' can be used to avoid th newline after the output
a = 0
b = 1
while a < 1000:
    print(a, end=',')
    a, b = b, a +b 