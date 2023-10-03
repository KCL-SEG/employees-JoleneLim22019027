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
    def __init__(self, name, salary, bonus=0, commission_per_contract=0, num_of_contracts=0):
        super().__init__(name)
        self.salary = salary
        self.bonus = bonus
        self.commission_per_contract = commission_per_contract
        self.num_of_contracts = num_of_contracts
        if self.bonus and (self.commission_per_contract == 0):
            Employee.set_pay(self, salary + self.bonus)
        elif (self.bonus == 0) and self.commission_per_contract:
            Employee.set_pay(self, salary + self.commission_per_contract * self.num_of_contracts)
        elif (self.bonus != 0 and self.commission_per_contract != 0):
            raise ValueError("A salary employee can only receive contract commission, bonus commission or no commission.")
        else:
            Employee.set_pay(self, salary)
    
    def __str__(self):
        if self.bonus and (self.commission_per_contract == 0):
            return (f'{Employee.get_name(self)} works on a monthly salary of {self.salary} and receives a bonus commission of {self.bonus}. Their total pay is {Employee.get_pay(self)}.')
        elif (self.bonus == 0) and self.commission_per_contract:
            return (f'{Employee.get_name(self)} works on a monthly salary of {self.salary} and receives a commission for {self.num_of_contracts} contract(s) at {self.commission_per_contract}/contract. Their total pay is {Employee.get_pay(self)}.')
        else:
            return (f'{Employee.get_name(self)} works on a monthly salary of {Employee.get_pay(self)}. Their total pay is {Employee.get_pay(self)}.')


class ContractEmployee(Employee):
    def __init__(self, name, pay_per_hour, hours_worked, bonus=0, commission_per_contract=0, num_of_contracts=0):
        super().__init__(name)
        self.pay_per_hour = pay_per_hour
        self.hours_worked = hours_worked
        self.bonus = bonus
        self.commission_per_contract = commission_per_contract
        self.num_of_contracts = num_of_contracts
        if self.bonus and (self.commission_per_contract == 0):
            Employee.set_pay(self, self.pay_per_hour*self.hours_worked + self.bonus)
        elif (self.bonus == 0) and self.commission_per_contract:
            Employee.set_pay(self, self.pay_per_hour*self.hours_worked + self.commission_per_contract * self.num_of_contracts)
        elif (self.bonus != 0 and self.commission_per_contract != 0):
            raise ValueError("A contract employee can only receive contract commission, bonus commission or no commission.")
        else:
            Employee.set_pay(self, self.pay_per_hour * self.hours_worked)

    def __str__(self):
        if self.bonus and (self.commission_per_contract == 0):
            return(f'{Employee.get_name(self)} works on a contract of {self.hours_worked} at {self.pay_per_hour}/hour and receives a bonus commission of {self.bonus}. Their total pay is {Employee.get_pay(self)}.')
        elif (self.bonus == 0) and self.commission_per_contract:
            return(f'{Employee.get_name(self)} works on a contract of {self.hours_worked} at {self.pay_per_hour}/hour and receives a commission for {self.num_of_contracts} contract(s) at {self.commission_per_contract}/contract. Their total pay is {Employee.get_pay(self)}.')
        else:
            return(f'{Employee.get_name(self)} works on a contract of {self.hours_worked} at {self.pay_per_hour}/hour. Their total pay is {Employee.get_pay(self)}.')


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryEmployee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = ContractEmployee('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryEmployee('Renee', 3000, 0, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = ContractEmployee('Jan', 25, 150, 0, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryEmployee('Robbie', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = ContractEmployee('Ariel', 30, 120, 600)