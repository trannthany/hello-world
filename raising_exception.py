# raise statement raises an exception
# print(1)
# raise ValueError
# print(2) # this statement won't get executed


# raise exception can be raised with arguments that give detail about them
# name = "123"
# raise NameError("Invalid name!")

# in except blacks, the raise statement can be used without arguments to reraise whatever exception occurred
try:
    num = 5/0
except:
    print("An error occurred")
    raise