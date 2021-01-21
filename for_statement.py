# # Strategy: Iterate over a copy
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]

# # Strategy: Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status

print("Range function")

for i in range(5):
    print(i)

# 5 is the end point but it does not include

a = ['Hello', 'darkness', 'my', 'old', 'friend']
for i in range(len(a)):
    print(i, a[i])
print(range(4))
print(sum(range(4))) # 0 + 1 + 2 + 3
print(list(range(4))) # this turns range to list [0, 1, 2, 3]
