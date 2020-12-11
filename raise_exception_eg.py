#create custom exception class
class CoffeeTooHotException(Exception):
    def __init__(self, msg):
        super().__init__(msg)



class CoffeeCup:
    def __init__(self, temperature):
        self.__temperature = temperature
    
    def drink_coffee(self):
        if self.__temperature > 85:
            #print('Coffee Too Hot') # instead of print something,we can raise exception
            #raise Exception # we can raise any Exception under the Exception class if you know, this way is not a good practice if you programme with other people
            #raise ValueError ('Coffee Too Hot') #this way of raising helps other programmer understand the error
            raise CoffeeTooHotException("Coffee Temperature: " + str(self.__temperature)) #this custome exception make the error very clear to other prammers
        elif self.__temperature < 65:
            #print('Coffee Too Cold')
            raise Exception
        else:
            print('Coffee Ok to Drink')

cup = CoffeeCup(105)
cup.drink_coffee()