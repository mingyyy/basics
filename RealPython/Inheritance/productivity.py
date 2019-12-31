class ProductivitySystem:
    def track(self, employees, hours):
        for employee in employees:
            employee.work(hours)
        print('')
