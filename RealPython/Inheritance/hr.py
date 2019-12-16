from abc import ABC, abstractmethod


class PayRollSystem:

    def calculate_payroll(self, employees):
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check Amount: {employee.calculate_payroll()}')
            print('')


class Employee(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @abstractmethod
    def calculate_payroll(self):
        pass


class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyEmployee(Employee):
    def __init__(self, id, name, hourly_rate, hours):
        super().__init__(id, name)
        self.hourly_rate = hourly_rate
        self.hours = hours

    def calculate_payroll(self):
        return self.hourly_rate * self.hours


class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        return super().calculate_payroll() + self.commission


# The DisgruntledEmployee class doesn’t derive from Employee,
# but it exposes the same interface required by the PayrollSystem
class DisgruntledEmployee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def calculate_payroll(self):
        return 100000
