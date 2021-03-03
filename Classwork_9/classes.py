# CamelCase
# camel_case
# sneak_case

# dunder


class Employee:
    def __init__(self, first_name, last_name=None):
        self.first_name = first_name
        self.last_name = last_name
        # self.full_name = f'{first_name} {last_name}'

    # def full_name(self, fallback_value='No last name.'):
    #     if self.last_name:
    #         return f'{self.first_name} {self.last_name}'
    #     return fallback_value

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @full_name.setter
    def full_name(self, value):
        self.first_name, self.last_name = value.split(' ')

    def __repr__(self):
        return f'<Employee first_name={self.first_name}, last_name={self.last_name}>'


emp1 = Employee('John', 'Doe')
# print(emp1.first_name, emp1.last_name)
# print(emp1)
# print(emp1.full_name())
print(emp1.full_name)
emp1.full_name = 'Davit Tovmasyan'
print(emp1.full_name)
print(emp1.first_name)

emp2 = Employee('Jane')
# print(emp2.first_name, emp2.last_name)
# print(emp2)
# print(emp2.full_name('Sorry no last name.'))
emp2.last_name = 'Doe'
print(emp2.full_name)
