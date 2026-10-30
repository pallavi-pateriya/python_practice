def handle_exception(a, b):
  a = int(a)
  b = int(b)

  try :
    res = a/b
    print(res)

  except ZeroDivisionError as e:
    print("Can not divide by zero")

  except InvalidNumber as e:
    print("enter valid digit")

  else :
    ("enter proper value")

handle_exception(10,0)


# Ask the user to enter their age and convert it to an integer. If they enter text such as "hello", catch the appropriate exception and print an error message.


def User(age):
    try:
        age = int(age)
        print(f"your age is {age}")
    except ValueError as e:
        print(f"The issue is {e}")
    except NameError as e:
        print(f"you got {e}")
    else:
        print("your age is found")
    finally:
        print("Done")

print("--- Testing invalid text string ---")
User("helo") 

print("\n--- Testing valid number ---")
User(10)


# Question 3: Handle missing dictionary keys
# Given this dictionary:
# Ask for a key and print its value. If the key doesn't exist, handle the exception without crashing.

user = {"name": "Monika", "age": 25}

def validate_key(d,k):
    try:
        print(d[k])
          
    except KeyError as e:
        print(f"not a key {e}")
           
validate_key(user,'a')

#custom exception

class MyCustomError(Exception):
    pass

def divide(a, b):
    if b == 0:
        raise MyCustomError("Division by zero is not allowed")
    return a / b
  

try:
    result = divide(10, 2)
    print(f"Result: {result}")
except MyCustomError as e:
    print(f"Caught an error: {e}")


