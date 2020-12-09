#unorder collection, no index, no duplication
A = {1, 2, 4, 5, 7, 9, 2}
print(A)

A.add(10)
print(A)

A.add(5)
print(A)

A.update([16,23,19,14])#add multiple values
print(A)

A.remove(14)#if 14 is not in the set it will cause an error
print(A)
A.discard(14)#if 14 is not in the set it will not cause an error
print(A)
A.remove(14)

A.pop() # will remove random element from the set

A.clear()
del A # delete the set

#using the set constructor
name = set(('max', 'tom', 'den'))

#convert list to set
Z = set([1,2,4,5])

# union
# A | B is the same as A.union(B)
# 
# intersection
# A & B is the same as A.intersection(B)
#
# Differe between 2 sets
# A - B is the same as A.difference(B)
#
# Symmetric difference
# A ^ B is the same as A.symmetric_difference(B)
