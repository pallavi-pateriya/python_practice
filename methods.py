# static method questions 

# Question 1: Calculator
# Create a Calculator class.
# Requirements:
# - Create a static method add(a, b) that returns the sum.
# - Create a static method multiply(a, b) that returns the product.
# - Call both methods without creating an object.

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def mul(a, b):
        return a * b

print(Calculator.add(10, 20))  # 30
print(Calculator.mul(10, 20))  # 200

# Question 2: Password Validator
# Create a User class.
# Requirements:
# - Create a static method is_valid_password(password).
# - Return True if the password has at least 8 characters; otherwise, return False.
# - Test it with "python123" and "abc".

class User:
  @staticmethod
  def is_valid_password(password):
    if len(password) >= 8:
      return True
    else :
      return False

print(User.is_valid_password('python123'))
print(User.is_valid_password('abc'))


#instance method questions

# Question 1: Student Grade Calculator
# Create a Student class.
# Requirements:
# - Initialize name and a list of marks.
# - Write an instance method calculate_average() to calculate the average marks.
# - Write an instance method get_grade() using these rules:
#   - Average 90 or above: A
#   - Average 75–89.99: B
#   - Average 60–74.99: C
#   - Average below 60: D
# - Create two students with different marks and print their averages and grades.


class Student:

    def __init__(self, name, list_of_marks):
        self.name = name
        self.list_of_marks = list_of_marks

    def calculate_average(self):
        total = sum(self.list_of_marks)
        self.avg = total / len(self.list_of_marks)
        return self.avg

    def get_grade(self):
        avg = self.calculate_average()

        if avg >= 90:
            return "A GRADE"
        elif avg >= 75:
            return "B GRADE"
        elif avg >= 60:
            return "C GRADE"
        else:
            return "D GRADE"


s1 = Student("Pallavi", [24, 25, 26])
s2 = Student("Monika", [90, 85, 95])

print(s1.calculate_average())
print(s1.get_grade())

print(s2.calculate_average())
print(s2.get_grade())


# create a BankAccount class.
# Requirements:
# - Initialize owner and balance through __init__().
# - Write a deposit(amount) method to increase the balance.
# - Write a withdraw(amount) method to decrease the balance only if sufficient funds are available.
# - Write a display_balance() method to print the current balance.

class BankAccount:

    def __init__(self, owner, balance):
      self.owner = owner
      self.balance = balance
          # self.amount = amount
    
    def deposit(self, amount):
      self.balance += amount
      print(f"Bank credited by {amount} your balance is {self.balance}")
  
    def withdraw(self, amount):
      if self.balance >= amount:
        self.balance -= amount
        print(f"withdraw of {amount} done your new balance is {self.balance}")
      elif amount < 0:
        print("enter valid amount")
      else :
        print("Can not Withdraw INSUFFICIENT BALANCE")
    
    def display_balance(self):
        print(f"{self.owner}'s current balance is {self.balance}")

b1=BankAccount('Pallavi', 80000)
b2=BankAccount('monika', 70000)
b1.deposit(10000)
b1.withdraw(100000)
b2.deposit(50000)


#class method questions


# Question 1: Employee Counter
# Create an Employee class.
# Requirements:
# - Create a class variable employee_count = 0.
# - Increase the count whenever an employee object is created.
# - Create a class method get_employee_count() that returns the total number of employees.
# - Create three employee objects and print the count.

class Employee:
    employee_count = 0

    def __init__(self, name):
        self.name = name
        Employee.employee_count += 1

    @classmethod
    def get_employee_count(cls):
        return cls.employee_count


e1 = Employee("Pallavi")
e2 = Employee("Monika")
e3 = Employee("Rahul")


# Question 2: Alternative Constructor
# Create a Student class with attributes name and marks.
# Requirements:
# - Write an __init__() method that accepts name and marks.
# - Create a class method from_string(data) that receives a string such as "Pallavi,85".
# - Split the string and use cls() to return a new Student object.
# - Print the student's name and marks.


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    @classmethod
    def from_string(cls, data):
        name, marks = data.split(",")
        return cls(name, int(marks))


student = Student.from_string("pallavi,85")

print(student.name)
print(student.marks)

