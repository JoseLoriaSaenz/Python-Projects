from Employee import Employee

class Company:
    def __init__(self):
        self.employees = []
    
    def add_employees(self, new_employee):
        self.employees.append(new_employee)

    def print_employees(self):
        for e in self.employees:
            print('Employee:', e.fname, e.lname, f'has a monthly salary of {e.paycheck():,.2f}')
        print('-----------')

def main():
    my_company = Company()
    
    employee1 = Employee('Sam', 'Smith', 65000)    
    my_company.add_employees(employee1)

    employee2 = Employee('Bob', 'Brown', 120000)    
    my_company.add_employees(employee2)

    my_company.print_employees()


main()
