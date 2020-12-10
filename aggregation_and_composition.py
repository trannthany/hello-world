class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay*12) + self.bonus


class Employee: #this Employee class acts as the container that contains Salary content
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.obj_salary = salary # Aggregation - (the Employee "has-a" Salary); "has-a" is a uni-direction
    
    def total_salary(self):
        return self.obj_salary.annual_salary()

# we are using composition concept, which mean we pass responsibility (deligate responsibility) from one class to another class

salary= Salary(2500, 500)
emp = Employee("Laura", 25, salary)
#both salary and emp will survive independly,
#whereas in the composition Salary is "part-of" Employee, if emp object is deleted then Salary's object will be deleted
print(emp.total_salary())