# List slices provide a more advanced way of retrieving values from a list
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6]) # from index 2 to index (6-1) 5???
print(squares[:6]) # take 6 length but only take from index 0 ?? [0, 1, 4, 9, 16, 25]
print(squares[3:8]) # take 8 length but only take from index 3 ?? [9, 16, 25, 36, 49]
# both statements do make sense but which one do most people percieve easily???

print(squares[0:1])

