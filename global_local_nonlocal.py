def funct():
    global x # we tell python use x from the global scope
    print('1 ----------',x)
    x  = 'This is a local variable' # now this uses the x from global variable and assigns a new value to it
    print('2 ----------',x) #the local has more priority 

x = 'This is a global variable'
funct()
print('3 ----------',x)