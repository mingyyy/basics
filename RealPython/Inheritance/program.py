import hr
import employee
import productivity

# salary_employee = hr.SalaryEmployee(1, 'John', 100)
# hourly_employee = hr.HourlyEmployee(2, 'Jen', 20, 10)
# commission_employee = hr.CommissionEmployee(3, 'Jess', 500, 20)
# disgruntled_employee = hr.DisgruntledEmployee(100, 'Anonymous')
# payroll_system = hr.PayRollSystem()
# payroll_system.calculate_payroll(
#     [
#         salary_employee,
#         hourly_employee,
#         commission_employee,
#         disgruntled_employee
#     ]
# )

manager = employee.Manager(1, 'John', 100)
secretary = employee.Secretary(2, 'Jen', 200)
sales_guy = employee.SalesPerson(3, 'Jess', 500, 200)
factory_worker = employee.FactoryWorker(4, 'Jane', 40, 15)
employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker
    ]
productivity_system = productivity.ProductivitySystem()
productivity_system.track(employees, 40)
payroll_system = hr.PayRollSystem()
payroll_system.calculate_payroll(employees)
