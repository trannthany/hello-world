#fh = open('demo.txt','w')
#fh = open('demo.txt', 'a')
#create demo.txt inside the same folder
#if there is no mod the default is read, we use 'w' because we want to write to thefile, w is responsible to make the demo.txt if it does exist
#fh is file handler

#fh.write('I write something to the file.\nI use python code to write this file.\nI"m so proud.\n')

# for i in range(10):
#     fh.write("This is line no %d\n" %(i+1))
# fh.close #close the file after you have written to the file, it is a good practice to free up the memory
# fh.write('I write something to the file.\nI use python code to write this file.\nI"m so proud.\n')
#The w mode will always replace the old file with a new one. 
#Use the a mode which will opens a file for appending, the file must already exist 

#this block of code is the same as a block code below
# fh = open('demo.txt', 'a')
# try:
#     for i in range(10):
#         fh.write("This is line no %d\n" %(i+1))
# finally:
#     fh.close()

#this block of code is the same as a block code above it
# with open('demo.txt', 'a') as fh: 
#     for i in range(10):
#         fh.write("This is line no %d\n" %(i+1))

#reading file
#fh = open('exact_path', 'mode of opening the file')
with open('demo.txt') as fh:#the default mode is the read mode
    #print(fh.read())#read() the whole content of the file
    
    #print(fh.readline()) #read first line if it uses for the first time
    #print(fh.readline()) #read second line if it uses for the second time
    
    #print(fh.readline(4))#read after the 4th character
    
    #print(fh.readlines())#read all the lines as a list
    #print(fh.readlines()[5])
    
    #iterate through the fh line by line
    for line in fh:
        print(len(line))
        print(line.split(' '))
