# https://www.youtube.com/watch?v=8DvywoWv6fI&t=6354s
"""
    Before we can read the contents of the file, we must tell Python which file we are going to work with and what we will be doing with the file.
    Thie is done with the open() function.
    The open() returns a "file handler" - a variable used to perform operations on the file.
    file_handler = open('file_name_and_its_path', 'mode')
    e.g. fh = open('mbox.txt', 'r') -- the mbox.txt is in the same directiory with the interpreter and the script, 'r' is the read mode.
    The read mode is used by default if the mode is not provided.

    \n is also character which is part of the whitespace
"""

"""
    Reading file
    xfile = open('mbox.txt')
    for a_line in xfile:
        print(a_line)
    
    fhand = open('mbox.txt')
    conout = 0
    for line in fhand:
        count = count + 1
    print('Line count: ', count)

    $python open.py

    You can read the whole file (newlines and all into a single string)
    fhand = open('mbox-short.txt')
    inp = fhand.read() #read() returns the whole text as a line of string
    print(len(inp))
    print(inp[:20])

    searching Through a file.
    We can put an if statement in our for loop to only print lines that meet some criteria.
    fhand = open('mbox-short.txt')
    for line in fhand:
        if line.startswith('From:') :
            print(line)

    Note: Each line from the file has a newline at the end. Moreover, the print statement adds a new line to each line.
    
    We can strip the whitespace from the right-hand side of the string usin rstrip() form the string library.
    The new line is considered "white space" and is stripped

    fhand = open('mbox-short.txt')
    for line in fhand:
        line = line.rstrip()
        if line.startswith('From:'):
            print(line)
    
    skipping with continue:
    We can conveniently skip a line by using the continue statement.
    
    fhand = open('mbox-short.txt')
    for line in fhand:
        line = line.rstrip()
        if not line.startswith('From:'):
            continue
        print(line)
    
    using in to select lines:
    we can look for a string anywhere in a line as our selection criteria.
    
    fhand = open('mbox-short.txt')
    for line in fhand:
        line = line.rstrip()
        if not '@uct.ac.za' in line:
            continue
        print(line)

    Bad file names:

    fname = input('Enter the file name: ')
    try:
        fhand = open(fname)
    except:
        print('File cannot be opened: ', fname)
        quit() # the quit() will stop the codes below getting invoked. fhand has not been defined. 
    
    count = 0
    for line in fhand:
        if line.startswith('Subject: '):
            count = count + 1
        
    print('There were', count, 'subject lines in', fname)

"""