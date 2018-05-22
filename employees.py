from datetime import date

class Employee:
  def __init__(self,name,title,start_date):
        self.name= name
        self.title= title
        self.start_date = start_date


class Company(object):
    """This represents a company in which people work"""

    def __init__(self, company_name, date_founded):
        self.company_name = company_name
        self.date_founded = date_founded
        self.employees = []

    def get_company_name(self):
        """Returns the name of the company"""

        return self.company_name

    # Add the remaining methods to fill the requirements above

    def add_employees(self,emps):
        self.employees.extend(emps)


emp1 = Employee("person","water",date.today())
emp2 = Employee("person2","waterPerson",date.today())
emp3 = Employee("person3","grassPerson",date.today())

go_co = Company("Go Company","2018")

go_co.add_employees([emp1,emp2,emp3])

print(go_co)