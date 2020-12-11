#json is text formate json javascripts text format
#there is a whole video to learn about json

import json

# a dictionary in python
# a = {
#     'name'      :   'Nadia',
#     'age'       :   23,
#     'marks'     :   [92, 97, 98, 91, 99],
#     'pass'      :   True,
#     'object'    :   {   'color'    :   ('red', 'blue')  }

# }
# # conver python dictionary into json
# print(json.dumps(a)) #cover python value into json value

# #dumps can take collecion data type and many more almost any value except set

# print(json.dumps(['1', '2']))
# print(json.dumps(('1', '2')))
# print(json.dumps("Hello World"))
# print(json.dumps(100))
# print(json.dumps(False))
# print(json.dumps(None))

# print(json.dumps(a, indent=4)) #4 indent for every element
#print(json.dumps(a, indent=4, separator=('. ', ' = '))) #use the original notation if you can
#print(json.dumps(a, indent=4, sort_keys=True))#put elements in order

#put json in json file
# with open('./json_data/demo.json', 'w') as fh:
#     fh.write(json.dumps(a, indent=2))


with open('./json_data/demo.json', 'r') as fh:
    json_str = fh.read()#fh.read() returns a string value
    json_value = json.loads(json_str)#converts a string into a json value (which was the python dictionary)
    #I convert it back into python dictionary
    print(type(json_value))
    print(json_value['name']) 
