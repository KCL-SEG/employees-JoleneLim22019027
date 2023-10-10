"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name
        self.totalPay = 0

    def get_name(self):
        return self.name
    
    def get_pay(self):
        return self.totalPay
    
    def set_name(self, newName):
        self.name = newName
    
    def set_pay(self, newPay):
        self.totalPay = newPay

class SalaryEmployee(Employee):
    def __init__(self, name, salary, commission=0, num_of_contracts=0):
        super().__init__(name)
        self.salary = salary
        self.commission = commission
        self.num_of_contracts = num_of_contracts
        if (self.commission > 0 and self.num_of_contracts == 0):
            Employee.set_pay(self, salary + self.commission)
        elif (self.num_of_contracts > 0):
            Employee.set_pay(self, salary + self.commission * self.num_of_contracts)
        else:
            Employee.set_pay(self, salary)
    
    def __str__(self):
        if (self.commission > 0 and self.num_of_contracts == 0):
            return (f'{Employee.get_name(self)} works on a monthly salary of {self.salary} and receives a bonus commission of {self.commission}. Their total pay is {Employee.get_pay(self)}.')
        elif (self.num_of_contracts > 0):
            return (f'{Employee.get_name(self)} works on a monthly salary of {self.salary} and receives a commission for {self.num_of_contracts} contract(s) at {self.commission}/contract. Their total pay is {Employee.get_pay(self)}.')
        else:
            return (f'{Employee.get_name(self)} works on a monthly salary of {self.salary}. Their total pay is {Employee.get_pay(self)}.')

class ContractEmployee(Employee):
    def __init__(self, name, pay_per_hour, hours_worked, commission=0, num_of_contracts=0):
        super().__init__(name)
        self.pay_per_hour = pay_per_hour
        self.hours_worked = hours_worked
        self.commission = commission
        self.num_of_contracts = num_of_contracts
        if (self.commission > 0 and self.num_of_contracts == 0):
            Employee.set_pay(self, self.pay_per_hour*self.hours_worked + self.commission)
        elif (self.num_of_contracts > 0):
            Employee.set_pay(self, self.pay_per_hour*self.hours_worked + self.commission * self.num_of_contracts)
        else:
            Employee.set_pay(self, self.pay_per_hour*self.hours_worked)

    def __str__(self):
        if (self.commission > 0 and self.num_of_contracts == 0):
            return (f'{Employee.get_name(self)} works on a contract of {self.hours_worked} hours at {self.pay_per_hour}/hour and receives a bonus commission of {self.commission}. Their total pay is {Employee.get_pay(self)}.')
        elif (self.num_of_contracts > 0):
            return (f'{Employee.get_name(self)} works on a contract of {self.hours_worked} hours at {self.pay_per_hour}/hour and receives a commission for {self.num_of_contracts} contract(s) at {self.commission}/contract. Their total pay is {Employee.get_pay(self)}.')
        else:
            return (f'{Employee.get_name(self)} works on a contract of {self.hours_worked} hours at {self.pay_per_hour}/hour. Their total pay is {Employee.get_pay(self)}.')


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryEmployee('Billie', 4000)
print(str(billie))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = ContractEmployee('Charlie', 25, 100)
print(str(charlie))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryEmployee('Renee', 3000, 200, 4)
print(str(renee))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = ContractEmployee('Jan', 25, 150, 220, 3)
print(str(jan))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryEmployee('Robbie', 2000, 1500)
print(str(robbie))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = ContractEmployee('Ariel', 30, 120, 600)
print(str(ariel))