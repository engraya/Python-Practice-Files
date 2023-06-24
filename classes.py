from xml.etree.ElementTree import Comment


class Payroll:

    def __init__(self, first_name, last_name, continent, country):
        self.first_name = first_name
        self.last_name = last_name
        self.continent = continent
        self.country = country

    def pay_package(self):
classes.py        full_name = self.first_name, self.last_name
        total_pay_details = f" The gross payment of the employee paid by {full_name}, in {self.country}, is by installment"
        print(total_pay_details)

    

employee1 = Payroll('Ahmad', 'Yakubu', 'Africa', 'Nigeria')
print(employee1.country)
employee1.pay_package()

