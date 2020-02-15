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


emp_1 = Employee('Correy', 'Strat', 1000)
emp_2 = Employee('shanon','stres', 999)

print(Employee.num_of_emps)
