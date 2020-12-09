print("Hello World")
x = 50
y = 10
print("{0} * {1} = {2}".format(x, y, x* y))
print ("Hello", "World", sep="====")

# C style string formating
name = "Max"
heigh = 1.79
print("Hello %s" % name) 
print("Hello %s ! are you %d years old" % (name, y))
print("%s is %.2f cm" % (name, heigh))

#user input
userInput = input("Enter some value:")
#input function take everything as a string
# casting ---   int(input("Enter some value:"))