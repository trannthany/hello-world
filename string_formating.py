# string formating - is a way to embed non-strings within strings.

nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}".format(nums[0], nums[1], nums[2])
print(msg)

print("{0}{1}{0}".format("abra","cad"))

# string formating can also be done with named arguments

a = "{x}, {y}".format(x=5, y=12)
print(a) 

str="{c}, {b}, {a}".format(a=5, b=9, c=7)
print(str)

#string functions
# join, replace, endswith, upper, lower, split etc ...