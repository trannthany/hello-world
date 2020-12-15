#why we need to know pdb? 
#because we normally run python script on a server which does not have an IDE


def add(x, y):
    sum = x + y
    return sum

def main():
    x = input("Num 1 : ")
    y = input("Num 2 : ")   
    z = add(x, y)
    print(z)

if __name__ == "__main__":
    # x = input("Num 1 : ")
    # y = input("Num 2 : ")
    # import pdb; pdb.set_trace() #this trick allows developer to locate and remove this line after the bug has been found
    # z = add(x, y)
    # print(z)
    main()

#to run pdb 
# python3 -m pdb name_file.py
# 
# another way to use pdb is to import it
# once you've imprted pdb then you don't need -m pdb flags
# just run python3 name_file.py 
# 
# another way is import your name_file.py and pdb in the python shell however we need to have a main() function that run the script for it to work
