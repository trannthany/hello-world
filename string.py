joke = 'Cruxifiction? Good. Line is on the left, one cross each.'
# for l in joke:
#     print(l)

print(joke[0:4]) #from 0 upto but not include 4 
print(joke[30:3000]) # it does not through error

print(joke[:15]) #from 0 upto but not include 15
print(joke[14:]) #from 14 and all the way to the end

print(joke[14::3]) # from 14, all the way to the end with 3 steps at a time

print('n' in joke)
print('cross' in joke)
print('banana' in joke)