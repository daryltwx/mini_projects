class Employee:

    num_of_emps = 0
    raise_amount = 1.04
        
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
        
class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    raise_amount = 1.20

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("--->", emp.fullname())


emp_1 = Employee("John", "Teo", 1200)
emp_2 = Employee("Test", "User", 20000)

dev_1 = Developer("John", "Teo", 1200, "Python")
dev_2 = Developer("Test", "User", 20000, "Java")

mgr_1 = Manager("Sue", "Smith", 90000, [dev_1])

# Check if class is a subclass
print(issubclass(Manager, Developer))












#### Learning ####


#Employee.set_raise_amount(1.1)

#emp_string_1 = "Steve-Smith-30000"

# new_emp_1 = Employee.from_string(emp_string_1)
# print(new_emp_1.email)

# import datetime
# my_date = datetime.date(2016, 7, 10)
# print(Employee.is_workday(my_date))


# print(mgr_1.email)
# mgr_1.add_emp(dev_2)
# mgr_1.print_emp()
# mgr_1.remove_emp(dev_1)
# print(" ")
# mgr_1.print_emp()