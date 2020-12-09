A = [0,1,2,3,4,5] # list
B = (0,1,2,3,4,5) # tuple
C = {0,1,2,3,4,5} # set
D = '012345' # string
E = {"name":"Max","age":20} #dictionary

for i in D:
    print(i)

for x in E.keys():
    print(x)

for y in E.values():
    print(y)

for z in E.items():
    print(z)

for k, v in E.items():
    print(k, ' ', v)

# range will start from 0 to 5
for j in range(6):
    print(j)

# range(start value, number of values, step)
for l in range(2,30,2):
    print(l)
else:
    print("finished")