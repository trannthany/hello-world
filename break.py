a = [0, 1, 2, 3, 4, 5]
for x in a:
    if x == 3:
        break
    print(x)

print('-------------------')
i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i+=1

print('-------------------')
for x in a:
    if x == 2:
        continue # continue will not execute any code that come after it but go to the next iteration (skipping)
    print(x)