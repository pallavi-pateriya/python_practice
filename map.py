# Q1. Square every number
# Use map() to return the square of each number.
# Expected val: [1, 2, 3, 4, 5]
# Expected output: [1, 4, 9, 16, 25]

val= [1, 2, 3, 4, 5]

def square(i):
  return i**2

l = list(map(square, val))
print(l)


# Q2. Convert numbers to strings
# Use map() to convert every integer to a string.
# Expected val: [10, 25, 0, -3]
# Expected output: ['10', '25', '0', '-3']

val = [10, 25, 0, -3]

def convert_to_string(i):
  return str(i)

l = list(map(convert_to_string, val))
print(l)

# Q3. Celsius to Fahrenheit
# Convert each temperature using F = (C × 9/5) + 32.
# Expected val: [0, 20, 30, 100]
# Expected output: [32.0, 68.0, 86.0, 212.0]

val = [0, 20, 30, 100]

def celsius_to_fahrenheit(i):
  F = (i * 9/5) + 32
  return F
  

l = list(map(celsius_to_fahrenheit, val))
print(l)


# Q4. Capitalize names
# Capitalize the first character of each single-word name.
# Expected val: ['ajay', 'pallavi', 'rohan']
# Expected output: ['Ajay', 'Pallavi', 'Rohan']

val = ['ajay', 'pallavi', 'rohan']

#using built in capitalize function
def capitalize_name(i):
    return i.capitalize()

l = (list(map(capitalize_name, val)))
print(l)


# using slicing and upper function
def func(i):
  name = i[0].upper() + i[1:]
  return name

l = (list(map(func, val)))
print(l)


# Q5. Calculate string lengths
# Return the length of each string.
# Expected val: ['python', 'map', 'programming']
# Expected output: [6, 3, 11]

val = ['python', 'map', 'programming']

def len_func(i):
  return len(i)

l = list(map(len_func, val))
print(l)

# Q6. Add corresponding elements
# Given equal-length lists, add values at matching positions.
# Expected val: a = [1, 2, 3, 4], b = [10, 20, 30, 40]
# Expected output: [11, 22, 33, 44]

a = [1, 2, 3, 4]
b = [10, 20, 30, 40]

def add_elements(i, j):
  return i + j

l = list(map(add_elements, a, b))
print(l)


# Q7. Extract first characters
# Extract the first character from each non-empty word.
# Expected val: ['apple', 'banana', 'cherry']
# Expected output: ['a', 'b', 'c']

val = ['apple', 'banana', 'cherry']

def extract_first_character(i):
  return i[0]

l=list(map(extract_first_character, val))
print(l)

# Q8. Apply a 10% discount
# Apply a 10% discount to each price and round to two decimal places.
# Expected val: [100, 249.99, 50]
# Expected output: [90.0, 224.99, 45.0]

val = [100, 249.99, 50]

def apply_discount(i):
  return round(i*0.9, 1)

l = list(map(apply_discount, val))
print(l)


# Q9. Normalize strings
# Strip leading/trailing whitespace and lowercase each string.
# Expected val: ['PYTHON', 'Map' 'FILTER']
# Expected output: ['python','map','filter']

val = ['PYTHON'   ,    'Map   ', 'FILTER  ']

def normalize_string(i):
  i = i.strip(" ").lower()
  return i

l = list(map(normalize_string, val))
print(l)


# Q10. Create item labels
# Convert each number to the format ['item-3', 'item-7', 'item-12']
# Expected val: [3, 7, 12]
# Expected output: ['item-3', 'item-7', 'item-12']

val = [3, 7, 12]

def create_item_label(i):
  i = f"item-{i}"
  return i

l = list(map(create_item_label, val))
print(l)




