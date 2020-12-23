#function is a way to store and reuse steps

def thing():
    print('Hello')
    print('Fun')


def say_hello(language):
    if (language == 'es'):
        return 'Ola'
    elif (language == 'fr'):
        return 'Bonjour'
    else:
        return 'Hello'
    

