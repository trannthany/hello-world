#Private members/attributes are private to the class
class Hello:
    def __init__(self, name):
        self.a = 10
        self._b = 20
        self.__c = 30
        self.__name = name
    
    def public_method(self):
        print(self.__c)
        print(self.a)
        print('This is from Hello class public method' )
        self.__private_method() #the private method can only be accessed inside its class

    def set_name(self, value):
        self.__name = value

    def get_name(self):
        return self.__name
    
    def __private_method(self):
        print('this is from Hello class private method')
    


hello = Hello('thany')
print(hello.a)
print(hello._b) 
hello.__name = 'Jonathan' 
print(hello.get_name())

hello.set_name('Jonathan') 

hello.public_method()
#hello.__private_method() this will throw AttributeErro because it private method cannot be access from outside the class