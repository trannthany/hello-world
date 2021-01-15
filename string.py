"""
    Ekke Ekke Ekke Ptang Zoo Boing!
    Strange woman lying in ponds distributing swords is no basis for a system of government.
    Supreme executive power comes from a mandate from the masses, not some farcical aquatic ceremony 
"""
joke = 'Crucifixion? - Yes - Good, out of the door, line on the left, one cross each.'
too_much_space = '                Hello World                   '
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

dir(joke) # shows all the methods that joke string can do
type(joke) # show the type of variable

#search and replace
new_joke = joke.replace("Good", "Excellent")
print(new_joke)
print(joke)

# lstrip() removes left white space, rstrip() removes right whitespace
# strip() removes both beginning and ending whitespace
print(too_much_space.lstrip())
print(too_much_space.rstrip())
print(too_much_space.strip())

print(joke.startswith("Crucifixion?"))
print(joke.startswith("C"))
print(joke.startswith("c"))

# find() returns the idex of the element
question_mark = joke.find('?')
print(question_mark)

#In python3 all strings are unicode