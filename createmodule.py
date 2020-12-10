import math 
#import imp
#import myfunctionsmodule #if this module is in the same folder as this file
#from functions import myfunctionsmodule #this doesn't work if you use function key word
#import dir.myfunctionsmodule
from dir import myfunctionsmodule as dummy

#imp.reload(mymodule)
#print(myfunctionsmodule.add(10, 59))
#print(myfunctionsmodule.multiply(10,3))
#math is a built in module
#this file and myfunctionsmodule are in the same folder

#assign to a local name if you need to use it more often
#add = myfunctionsmodule.add

#print(add(5,8))


#add = dir.myfunctionsmodule.add
#print(add(5,8))

multiply = dummy.multiply
print(multiply(6,6))