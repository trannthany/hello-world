astring = input("Enter a number: ")

try:
    num = int(astring)
except:
    num = -1

print(num)