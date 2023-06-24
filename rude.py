import funcs

funcs.strategy()

from classes import Payroll

intern = Payroll('mehmet', 'akbaba', 'europe', 'turkey')
print(intern.country)
intern.pay_package()