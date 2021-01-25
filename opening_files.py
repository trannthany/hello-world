# myfile = open("path/to/the/file.txt")

# # write mode
# open("filename.txt", "w")

# # read mode
# open("filename.txt", "r")
# open("filename.txt")

# # binary write mode
# open("filename.txt", "wb")

#You can use the + sign with each of the modes above to give them extra access to files. For example, r+ opens the file for both reading and writing.


# Once a file has been opened and used, you should close it
# file = open("filename.txt", "w")
# # do stuff to the file
# file.close()



## Reading files
file = open("test.txt", "r")
#cont = file.read()
#print(cont) # this will print all of the contents of the file "test.txt"

# print(file.read(16)) # print 16 characters
# print(file.read(4))
# print(file.read(4))
# # You can make more calls to read on the same file object to read more of the file byte by byte

# print(file.read()) # without an argument read returns the rest of the file

########
# for i in range(21):
#   print(i, file.read(4))

# print(file.read())

# print(file.read(6)) # any read after all the contents in the file have been read, will return an empty string
# # Because it is the end of the file
##############

##############
# To retrieve each line in a file, you can use the readlines method to return a list in which each element is a line in the file




file.close()

#############
# To write a files you use the write method, which writes a string to the file

# file = open("newfile.txt", "w")
# file.write("This has been written to a file")
# file.close()

# file = open("newfile.txt", "r")
# print(file.read())
# file.close()

## **** When a file is opened in write mode, the file's existing content is deleted **** 
# file = open("newfile.txt", "w")
# file.write("Some new text")
# file.close()

# file = open("newfile.txt", "r")
# print("reading new content")
# print(file.read())
# file.close()

# The "This has been written to a file" disappears

## To write something other than a string, it needs to be converted to a string first

# msg = "Hello world!!"
# file = open("newfile.txt", "w")
# amount_written = file.write(msg)
# print(amount_written)
# file.close()

# if a file write operation is successful, which one of these statements will be true?
# file.write(msg) == len(msg)


## use try, except and finally when working with files
try:
    msg = "Hello world!!"
    file = open("newfile.txt", "w")
    amount_written = file.write(msg)
    print(amount_written)
finally:
    file.close()

# The finally will always ensure that the file is close at the end

# The alternative way is to use with statements
with open("newfile.txt") as f:
    print(f.read())   