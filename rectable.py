class Rectangle:
    pass 

rect1 = Rectangle()
rect2 = Rectangle()

rect1.height = 20
rect2.height = 30

rect1.width = 40
rect2.width = 10

rect1.area = rect1.height * rect2.width 
print(rect1.area)