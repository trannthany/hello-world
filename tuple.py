#tuple cannot be change, list can be changed
# tuple are similar to list
#
x = (1, 5, 3, 4, 8)

print(x[2])

y = (3, 'max', 'Nadia', 15.6, 990, True) 
print(y.count(3)) # count how many 3 in the tuple

z = x + y
print(z)

a = ('hi',) * 5
print(a)

del a

print(a)