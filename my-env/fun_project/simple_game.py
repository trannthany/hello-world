def get_input():
    command = input(": ").split()
    verb_word = command[0]
    if verb_word in verb_dict:
        verb = verb_dict[verb_word]
    elif verb_word == "q":
        return 'q'
    else:
        print("Unknown verb {}".format(verb_word))
        return
    
    if len(command) >= 2:
        noun_word = command[1]
        print(verb(noun_word))
    else:
        print(verb("nothing"))

def say(noun):
    return 'You said "{}"'.format(noun)

def shout(noun):
    return 'You shout "{}"'.format(noun)

verb_dict = {
    "say":say,
    "shout": shout
}

while True:
    if get_input() == 'q':
        break

