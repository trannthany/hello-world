x = [3, 5, 4, 9, 10]
print(x)
print(x[3])

y = ['max', 1, 15.5, [4,5]]
print(y[0])
print(y[3][1])

print(len(y))
print(len(y[3]))

x.insert(2, "Tom")
print(x)

x.remove('Tom')
print(x)

x.insert(3, 3)
print(x)

x.remove(3) # it will remove the first value which is found on the left first
print(x)

z = x.pop() # remove the last value from the list like a stack
print(x)
print(z)

a = x # or a = x.copy
a.clear() # remove everything
print(a)

x.sort() #sort in ascending order
x.reverse #reverse the order
x.append(10)#add to the the list on the right
x.count(10)#count how many 10 in the list
