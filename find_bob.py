# def find_bob(names):
#     i = 0
#     while i < len(names):
#         if(names[i] == 'Bob'):            
#             return i
#         i += 1
#     return -1
        


# print(find_bob(["Jimmy", "Layla", "Bob"]))
# print(find_bob(["Bob", "Layla", "Kaitlyn", "Patricia"]))
# print(find_bob(["Jimmy", "Layla", "James"]))

# def factorial(num):
#     sum = 1

#     for i in range (num):
#         sum *= (i+1)

#     print(sum)    


# factorial(3)
# factorial(5)
# factorial(13)


# def profit(info):
#     return round((info["sell_price"] - info["cost_price"]) * info["inventory"])




# a = profit({
#   "cost_price": 32.67,
#   "sell_price": 45.00,
#   "inventory": 1200
# })

# b = profit({
#   "cost_price": 225.89,
#   "sell_price": 550.00,
#   "inventory": 100
# })

# c = profit({
#   "cost_price": 2.77,
#   "sell_price": 7.95,
#   "inventory": 8500
# })

# print(a)
# print(b)
# print(c)

# fib = {1: 1, 2: 1, 3: 2, 4: 3}

# print(fib.get(4, 0) + fib.get(7, 5))

user_input = input('Enter a number: ')
try:
    val = int(user_input)
except:
    val = -1

if val > 0:
    print("Thanks for following the instruction!!!")
else:
    print('Read the instruction!!')