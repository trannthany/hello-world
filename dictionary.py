# dictionary is an associate list or a map (list of key-value pairs) {'keyname':'value', ....}
# any value can be used as a key
Dictionary = {'name': 'max', 'age':14, 'year':2004}
print(Dictionary['age'])
print(Dictionary['name'])

E = {'name':'Tom', 15:15, 15.1:15.1, True:True, (2,3):5}

print(E[True])


#add a new key
Dictionary['Surname'] = 'Tesar'
print(Dictionary)

#pop removes the key-value pair
a = Dictionary.pop('Surname')

#update a value
Dictionary['name'] = 'Tom'
Dictionary.update({'age': 23})
print(Dictionary)

#list all the keys in the dictionary
Dictionary.keys()

#list all the values in the dictionary
Dictionary.values()

#list all the key-values pair
Dictionary.items()

#remove and return the last key-value pair
Dictionary.popitem()