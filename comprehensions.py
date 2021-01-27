# one line initialisation of tuble, list or dictionary

x = [x for x in range(5)]
print(x)

y = [ a for a in range(100) if a % 5 == 0]
print(y)
print(len(y))
z = [x % 5 for x in range(100)]
print(z)
print(len(z))