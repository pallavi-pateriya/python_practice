from functools import reduce

# Q1. Sum all numbers
# Calculate the sum of all numbers.
# Expected input: [1, 2, 3, 4, 5]
# Expected output: 15

val = [1, 2, 3, 4, 5]

def sum(i,j):
  return i + j

l = reduce(sum, val)
print(l)


# Q2. Calculate product
# Multiply all numbers together.
# Expected input: [2, 3, 4, 5]
# Expected output: 120

val = [2, 3, 4, 5]

def product(x, y):
  return x * y

p = reduce(product, val)
print(p)


# Q3. Find the maximum
# Find the largest number without using max(). Assume a non-empty list.
# Expected input: [12, 45, 7, 89, 34]
# Expected output: 89

val = [12, 45, 7, 89, 34]

def find_max_value(x, y):
  max = float('-inf')
  if x > y:
    max = x
  else :
    max = y
  return max

m = reduce(find_max_value, val)
print(m)


# Q4. Join words
# Combine words into one string with a single space between them.
# Expected input: ['Python', 'is', 'easy', 'to', 'learn']
# Expected output: 'Python is easy to learn'

val = ['Python', 'is', 'easy', 'to', 'learn']

def join_words(x, y):
  return x + " " + y

print(reduce(join_words, val))


# Q5. Count total characters
# Calculate the total number of characters across all strings.
# Expected input: ['map', 'filter', 'reduce']
# Expected output: 15

val = ['map', 'filter', 'reduce']

def count_total_char(x, y):
  return x + len(str(y))

print(reduce(count_total_char, val, 0))


# Q6. Flatten lists
# Combine a list of lists into one list.
# Expected input: [[1, 2], [3], [4, 5, 6]]
# Expected output: [1, 2, 3, 4, 5, 6]

val = [[1, 2], [3], [4, 5, 6]]

def flatten_list(x, y):
  x.extend(y)
  return x

print(reduce(flatten_list, val, []))


# Q7. Calculate factorial
# Calculate n! by reducing integers from 1 through n. Assume n >= 1.
# Expected input: n = 5
# Expected output: 120

n = 5
def factorial(x, y):
  return x*y

print(reduce(factorial, range(1, n+1)))


# Q8. Build a frequency dictionary
# Create a dictionary counting each word's occurrences.
# Expected input: ['cat', 'dog', 'cat', 'bird', 'dog', 'cat']
# Expected output: {'cat': 3, 'dog': 2, 'bird': 1}


val = ['cat', 'dog', 'cat', 'bird', 'dog', 'cat']

def generate_dict(x, y):
  if y in x:
    x[y] += 1
  else :
    x[y] = 1
  return x

print(reduce(generate_dict, val, {}))



# Q9. Find the longest word
# Return the longest word. If tied, return the first word of that length.
# Expected input: ['code', 'python', 'map', 'dictionary']
# Expected output: 'dictionary'

val = ['code', 'python', 'map', 'dictionary']

def longest_word(x, y):
  max = ''
  if len(y) > len(x):
    max = y
  else :
    max = x
  return max
  
    

print(reduce(longest_word, val))


# Q10. Concatenate digits
# Join digits into a string, preserving their order.
# Expected input: [2, 0, 2, 6]
# Expected output: '2026'

val = [2, 0, 2, 6]

def concatenate_digits(x, y):
  return str(x) + str(y)

print(reduce(concatenate_digits, val))
