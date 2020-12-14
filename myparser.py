import argparse

if __name__ == '__main__':
    #initialize the parser
    parser = argparse.ArgumentParser(
        description = "my math script"
    )

    #Add the parameters positional/optional (--num1, --num2, --operation mean they are operational parameter)
    parser.add_argument('-n','--num1', help="Number 1", type=float)
    parser.add_argument('-i','--num2', help="Number 2", type=float)
    parser.add_argument('-o','--operation', help="provide operator", default='+')
    # parse the arguments
    args = parser.parse_args()
    print(args)
    result = None
    if args.operation == '+':
        result = args.num1 + args.num2
    if args.operation == '-':
        result = args.num1 - args.num2
    if args.operation == '*':
        result = args.num1 * args.num2
    if args.operation == '/':
        result = args.num1 / args.num2    

    print(result)

# when run in the terminal
# (my-env) odoo14@odoo14-VirtualBox:~/learnPython3$ python3 myparser.py -n=84 -i=70 -o=+
# Namespace(num1=84.0, num2=70.0, operation='+')
# 154.0
# (my-env) odoo14@odoo14-VirtualBox:~/learnPython3$ python3 myparser.py -n=84 -i=70 -o=*
# Namespace(num1=84.0, num2=70.0, operation='*')
# 5880.0
