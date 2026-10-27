
# 1. Create a dictionary where numbers are keys and their squares are values.
d = {i: i**2 for i in range(1, 6)}
print(d)

# 2. Create a dictionary where numbers are keys and their cubes are values.
numbers = [1, 2, 3, 4, 5]
d = {i: i**3 for i in numbers}
print(d)

# 3. Create a dictionary where names are keys and their lengths are values.
names = ['apple', 'banana', 'kiwi', 'cat']
d = {i: len(i) for i in names}
print(d)

# 4. Create a dictionary containing only even numbers and their squares.
numbers = [1, 2, 3, 4, 5, 6]
d = {i: i**2 for i in numbers if i % 2 == 0}
print(d)

# 5. Create a dictionary containing students who scored 60 or above.
marks = {'Amit': 75, 'Riya': 45, 'Neha': 90, 'Raj': 55}
d = {key: value for key, value in marks.items() if value >= 60}
print(d)

# 6. Increase every product price by 10.
prices = {'apple': 50, 'banana': 30, 'mango': 80}
d = {key: value + 10 for key, value in prices.items()}
print(d)

# 7. Multiply every value in the dictionary by 10.
data = {'a': 2, 'b': 4, 'c': 6}
d = {key: value * 10 for key, value in data.items()}
print(d)

# 8. Create a dictionary where each word is a key and its uppercase version is the value.
words = ['python', 'django', 'fastapi']
d = {item: item.upper() for item in words}
print(d)

# 9. Create a dictionary containing only odd numbers, with 'odd' as each value.
numbers = [1, 2, 3, 4, 5, 6, 7]
d = {i: 'odd' for i in numbers if i % 2 != 0}
print(d)

# 10. Increase salaries by 10% only for employees earning 60000 or more.
employees = {'Amit': 50000, 'Riya': 65000, 'Neha': 80000, 'Raj': 55000}
d = {key: value*1.1 for key, value in employees.items() if value >= 60000}
print(d)
