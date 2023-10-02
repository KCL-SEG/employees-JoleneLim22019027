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

    def __str__(self):
        pass

class SalaryEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        Employee.totalPay = salary
    
    def __str__(self): 
        self.name, "works on a monthly salary of", self.salary, ". Their total pay is ", self.salary, "."

class SalaryEmployee(Employee):
    def __init__(self, name, salary, commission_per_contract, contracts):
        super().__init__(name)
        self.totalPay = salary + commission_per_contract*contracts
        self.salary = salary
        self.commission_per_contract = commission_per_contract
        self.number_of_contracts = contracts
    
    def __str__(self):
        return self.name, " works on a monthly salary of ", self.salary, " and receives a commission for ", self.number_of_contracts, " contract(s) at ", self.commission_per_contract, "/contract. Their total pay is ", self.salary, "."
    
class SalaryEmployee(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name)
        self.totalPay = salary + bonus
        self.salary = salary
        self.bonus_commission = bonus

    def __str__(self):
        return self.name, " works on a monthly salary of ", self.salary, " and receives a bonus commission of ", self.bonus_commission, ". Their total pay is ", self.totalPay, "."

class ContractEmployee(Employee):
    def __init__(self, name, pay_per_hour, hours_worked):
        super().__init(name)
        self.totalPay = pay_per_hour * hours_worked
        self.pay_per_hour = pay_per_hour
        self.hours_worked = hours_worked
    
    def __str__(self):
        return self.name, " works on a contract of ", self.pay_per_hour, "/hour. Their total pay is ", self.hours_worked, "."

class ContractEmployee(Employee):
    def __init__(self, name, pay_per_hour, hours_worked, commission_per_contract, contracts):
        super().__init(self, name)
        self.totalPay = pay_per_hour * hours_worked + commission_per_contract * contracts
        self.pay_per_hour = pay_per_hour
        self.hours_worked = hours_worked
        self.commission_per_contract = commission_per_contract
        self.number_of_contracts = contracts
    
    def __str__(self):
        return self.name, " works on a contract of ", self.pay_per_hour, "/hour and receives a commission for ", self.number_of_contracts, " contract(s) at ", self.commission_per_contract, "/contract. Their total pay is ", self.hours_worked, "."

class ContractEmployee(Employee):
    def __init__(self, name, pay_per_hour, hours_worked, bonus):
        super().__init__(name)
        self.totalPay = pay_per_hour * hours_worked + bonus
        self.pay_per_hour = pay_per_hour
        self.hours_worked = hours_worked
        self.bonus_commission = bonus
    
    def __str__(self):
        return self.name, " works on a contract of ", self.pay_per_hour, "/hour and received a bonus commission of ", self.bonus_commission, ". Their total pay is ", self.totalPay, "."

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryEmployee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = ContractEmployee('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryEmployee('Renee', 3000, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = ContractEmployee('Jan', 25, 150, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryEmployee('Robbie', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = ContractEmployee('Ariel', 30, 120, 600)
