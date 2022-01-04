class Person:
  def __init__(self, firstName, lastName):
    self.firstName = firstName
    self.lastName = lastName
    self.emailId = firstName.lower() + '.' + lastName.lower() + '@' + 'company.org'

firstName = input("First name: ")
lastName = input("Last name: ")

p1 = Person(firstName, lastName)

print(p1.firstName)
print(p1.lastName)
print(p1.emailId)