# #break
# while True:
#     line = input('> ')
#     if line == 'done':
#         break
#     print(line)

# print("We are done!")

# #continue did not break the loop, but it goes back to the top of the loop
# while True:
#     line = input('> ')
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print(line)

# print('We are done!!')

#definite loop

for i in [5, 4, 3, 2, 1]:
    print(i)

print('Why are you running?')

friends = ['Jonathan', 'Arwin', 'Ben']
for friend in friends:
    print('Marry Christmas', friend)

# i and friend are iteration variables

# def factorial_1(num):
#     sum = 1
#     for i in range(num):
#         sum *= (i + 1)
#     return sum

# def factorial_2(num):
#     sum = 1
#     while num > 0:
#         sum *= num
#         num -= 1
#     return sum

# print(factorial_1(12))
# print(factorial_2(12))
# print(factorial_1(6))
# print(factorial_2(6))

# the is the stroger operator than ==, and it is used for None and boolean types, use == for string and integers etc.
# is not is the opposite
smallest = None # this a good technique to find the largest number also.
for num in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num
    print(smallest, num)

print('After', smallest)