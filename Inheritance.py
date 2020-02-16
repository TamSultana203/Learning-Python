class Employee:

    raise_amount = 1.04

    def  __init__(self, first, last, pay):
        self.first =first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)


#developer subclass inherites from employee class

class Developer(Employee):
    raise_amount = 1.10

    def  __init__(self, first, last, pay, prog_lang):
        super(self, prog_lang).__init__()
        self.prog_lang = prog_lang

dev_1 = Developer('Correy', 'Strat', 1000, 'Python')
dev_2 = Developer('shanon','stres', 999, 'Java')

#print(dev_1.email)
#print(dev_2.email)
# print(help(Developer)) used to see whats inherited from where

#print(dev_1.pay)
#dev_1.apply_raise()
#print(dev_1.pay)

print(dev_1.email)
print(dev_1.prog_lang)
