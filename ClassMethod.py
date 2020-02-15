#regular method automatically pass the instance as first argument we call self
#class method automatically pass the class as first to argument, we that cls
#static method dont pass instance or class

class Employee:
    raise_amount = 1.04
    num_of_emps = 0
    def  __init__(self, first, last, pay):
        self.first =first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@gmail.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise (self):
        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


emp_1 = Employee('Correy', 'Strat', 1000)
emp_2 = Employee('shanon','stres', 999)




emp_str_1 = 'John-Doe-7000'
emp_str_2 = 'Steve-smith-3500'
emp_str_3 = 'Jane-doe-9000'

new_emp_1 = Employee.from_string(emp_str_1)  #class method

print(new_emp_1.email)
print(new_emp_1.pay)
#Employee.set_raise_amt(1.05)
#print(Employee.raise_amount)
#print(emp_1.raise_amount)
#print(emp_2.raise_amount)
