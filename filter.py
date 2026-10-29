# Q1. Keep even numbers
# Keep only even integers.
# Expected input: [1, 2, 3, 4, 5, 6, 7, 8]
# Expected output: [2, 4, 6, 8]

val = [1, 2, 3, 4, 5, 6, 7, 8]

def keep_even(i):
  if i % 2 == 0:
    return i

l=list(filter(keep_even, val))
print(l)


# Q2. Keep positive numbers
# Remove zero and negative numbers.
# Expected input: [-5, 0, 3, 8, -2, 1]
# Expected output: [3, 8, 1]

val = [-5, 0, 3, 8, -2, 1]

def keep_positive(i):
  if i > 0:
    return i

l = list(filter(keep_positive, val))
print(l)


# Q3. Filter words by length
# Keep words with more than five characters.
# Expected input : ['appple', 'orange', 'banana', 'kiwi', 'fgh']
# Expected output : ['orange', 'banana']

val =['apple', 'orange', 'banana', 'kiwi', 'fgh']

def filter_by_length(i):
  if len(i) > 5:
    return i

l = list(filter(filter_by_length, val))
print(l)


# Q4. Numbers divisible by 3
# Keep numbers divisible by 3 without a remainder.
# Expected input: [3, 7, 9, 10, 12, 14, 18]
# Expected output: [3, 9, 12, 18]

val = [3, 7, 9, 10, 12, 14, 18]

def divisible_by_3(input):
  if input % 3 == 0:
    return input

l = list(filter(divisible_by_3, val))
print(l)


# Q5. Names starting with A
# Keep names beginning with A, ignoring case.
# Expected input: ['ajay', 'rohan', 'pavan' 'Aman', 'riya','anita']
# Expected output: ['ajay','aman', 'anita']

val = ['ajay', 'rohan', 'pavan', 'Aman', 'riya','anita']

def keep_names_starting_with_a(i):
  if i[0] == 'a' or i[0] == 'A':
    return i

l = list(filter(keep_names_starting_with_a, val))
print(l)


# Q6. Passing scores
# Keep scores greater than or equal to 40.
# Expected input: [25, 40, 58, 39, 90, 33]
# Expected output: [40, 58, 90]

val = [25, 40, 58, 39, 90, 33]

def keep_passing_scores(i):
  if i >= 40:
    return i

l = list(filter(keep_passing_scores, val))
print(l)



# Q7. Remove empty strings
# Remove empty and whitespace-only strings.
# Expected input: ['hello', '', ' ', 'python', ' map ']
# Expected output: ['hello', 'python', ' map ']

val =  ['hello', '', ' ', 'python', ' map ']

def remove_trailing_whitespace(i):
    if i.strip():
        return i
  

l=list(filter(remove_trailing_whitespace, val))
print(l)


# Q8. Numbers within a range
# Keep integers from 10 through 50, inclusive.
# Expected input: [5, 10, 25, 50, 51, 100, 42]
# Expected output: [10, 25, 50, 42]

val = [5, 10, 25, 50, 51, 100, 42]

def num(i):
  if i in range(10,51):
    return i

l = list(filter(num, val))
print(l)


# Keep people whose age is at least 18.
# Expected input: [{'name': 'Asha', 'age': 17}, {'name': 'Ravi', 'age': 21}, {'name': 'Mina', 'age': 18}]
# Expected output: [{'name': 'Ravi', 'age': 21}, {'name': 'Mina', 'age': 18}]


val = [{'name': 'Asha', 'age': 17}, {'name': 'Ravi', 'age': 21}, {'name': 'Mina', 'age': 18}]

def filter_by_age(i):
  for key, value in i.items():
    if key == 'age' and value >= 18:
      return i

l = list(filter(filter_by_age, val))
print(l)


# Q10. Words containing a vowel
# Keep words containing a, e, i, o, or u, ignoring case.
# Expected input: ['sky', 'tree', 'rhythm', 'cloud', 'myth']
# Expected output: ['tree', 'cloud']

val = ['sky', 'tree', 'rhythm', 'cloud', 'myth']

def word_contains_vowel(i):
  for ch in i:
    if ch in 'aeiou':
      return i

l = list(filter(word_contains_vowel, val))
print(l)