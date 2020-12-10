class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return (self.pay*12) + self.bonus


class Employee: #this Employee class act as the container that contain Salary content
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        self.obj_salary = Salary(pay, bonus)
    
    def total_salary(self):
        return self.obj_salary.annual_salary()

# we are using composition concept, which mean we pass responsibility (deligate responsibility) from one class to another class


emp = Employee("Laura", 25, 2500, 500)
print(emp.total_salary())