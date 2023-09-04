from Employee import Employee, SalaryEmployee, HourlyEmployee, CommisionEmployee

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print('Current Employees')
        for e in self.employees:
            print(e.fname, e.lname)
        print('------------')

    def pay_employees(self):
        print('-----------------------')
        print('Paying Employees:')
        for e in self.employees:
            print('Paycheck for:', e.fname, e.lname)
            print(f'Amount: ${e.calculate_paycheck():,.2f}')
            print('-----------------------')

def main():
    my_company = Company()

    e1 = SalaryEmployee('Sarah', 'Hess', 65000)
    e2 = HourlyEmployee('Peter', 'Brown', 45, 60)
    e3 = CommisionEmployee("Gina", "Torres", 48500, 5, 215)
    
    my_company.add_employee(e1)
    my_company.add_employee(e2)
    my_company.add_employee(e3)

    my_company.display_employees()
    my_company.pay_employees()

main()
