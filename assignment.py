"""You are required to create a CommissionEmployee class in Python to represent an employee who
earns compensation based on a percentage of their total sales. The class must enforce encapsulation
principles by restricting direct access to sensitive attributes."""

class CommissionEmployee:

    def __init__(self,first_name,last_name,social_security_number, gross_sales, commission_rate):
        self.first_name = first_name
        self.last_name = last_name
        self.social_security_number = social_security_number
        self.__gross_sales = gross_sales
        self.__commission_rate = commission_rate

    def get_gross_sales(self):
        return self.__gross_sales

    def set_gross_sales(self, value):
        if value <= 0.0:
            print("Gross sales must be more than zero")
        else:
            self.__gross_sales = value

    def get_commission_rate(self):
        return self.__commission_rate

    def set_commission_rate(self, value):
        if 0.0 < value <= 1.0:
            self.__commission_rate = value
        else:
            print("Commission rate must be between 0.0 and 1.0")

    def display_employee(self):
       print(f"{self.first_name},{self.last_name}, {self.social_security_number}, {self.__gross_sales}, {self.__commission_rate}")

    def earnings(self):
        return self.__gross_sales * self.__commission_rate

class BasePlusCommissionEmployee(CommissionEmployee):
        def __init__(self,first_name,last_name,social_security_number, gross_sales, commission_rate, _base_salary):
            super().__init__(first_name, last_name, social_security_number,gross_sales, commission_rate)
            self.__base_salary = _base_salary

        def earnings(self):
            #total earnings = base salary + earnings from commissions
            return self.__base_salary + super().earnings()

        def set_base_salary(self, new_salary):
            if new_salary >= 0:
                self.__base_salary = new_salary
            else:
                print("Base salary must be greater than or equal to zero")

        def get_base_salary(self):
            return self.__base_salary

        def display_employee(self):
            super().display_employee()
            print(f"Base Salary: {self.__base_salary}")


emp1 = CommissionEmployee("Daniel", "Akaba", 34343422, 145072.0,0.25)
emp1.display_employee()
emp1.
print(emp1.earnings())

emp2 = BasePlusCommissionEmployee ("Abena", "Joyce", 23443545, 433342, 0.24, 3000)
emp2.display_employee()
print(emp2.earnings())
emp2.set_base_salary(5003)
print(f"Updated earnings {emp2.earnings()}")
print(f"updated name {emp2.first_name}")