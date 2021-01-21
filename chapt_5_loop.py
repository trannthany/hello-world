#while loop
# n = 5
# while n > 0:
#     print(n)
#     n = n - 1
# print("Blastoff!")
# print(n)

# while True:
#     line = input('Enter done to quite > ')
#     if line == 'done':
#         break
#     elif line == 'continue':
#         continue
#     print(line)
# print('Done!')

#definite loop (for loop)
# for i in [5, 4, 3, 2, 1]:
#     print(i)
# print('Ni')

# friends = ['Joseph', 'Glenn', 'Sally']
# for friend in friends:
#     print('Happy New Year: ', friend)
# print('Done!')

# friend is the Iteration variable
# friends is the list


def find_large_number(num_list):
   # large = num_list[0]
    large = None
    for n in num_list:
        # if n > large:
        #     large = n
        if large is None:
            large = n
        elif n > large:
            large = n
    
    return large

def find_small_number(num_list):
    #small = num_list[0]
    small = None
    for n in num_list:
        # if n < small:
        #     small = n
        if small is None:
            small = n
        elif n < small:
            small = n
    
    return small
# is operator implies "is the same as", is is similar to, but stronger than ==
# 0 == 0.0 is True, but 0 is 0.0 is False, is is good for boolean and None
# is not also is a logical operator
my_num_list = [9, 0, 3, -4, 8, 11, 6 , 97, 9, 0]
big = find_large_number(my_num_list)        
print(big)
small = find_small_number(my_num_list)
print(small)
