# Q1. Count the frequency of each item
# Build a dictionary mapping each item to the number of times it appears. The order of keys does not matter.
# Expected input: ["apple", "banana", "apple", "orange", "banana", "apple"]
# Expected output: {"apple": 3, "banana": 2, "orange": 1}


input = ["apple", "banana", "apple", "orange", "banana", "apple"]

def func(args):
  output = {}
  for i in args:
    if i not  in output:
      output[i] = 1
    else :
      output[i] += 1
  return output

print(func(input))


# Q2. Invert a dictionary with duplicate values
# Invert a dictionary so each original value maps to a list of all keys that had that value.
# Expected input: {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
# Expected output: {1: ['a', 'c'], 2: ['b', 'e'], 3: ['d']}

input = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}

def func(kwargs):
  output = {}
  for key, value in kwargs.items():
    if value not in output:
      output[value] = [key]
    else :
      output[value].append(key)
  
  return output

print(func(input))



# Q3. Merge dictionaries by summing common keys
# Merge two dictionaries. If a key appears in both, add the values; otherwise keep the available value.
# Expected input: d1 = {'apple': 3, 'banana': 2}, d2 = {'banana': 5, 'orange': 4}
# Expected output: {'apple': 3, 'banana': 7, 'orange': 4}

d1 = {'apple': 3, 'banana': 2}
d2 = {'banana': 5, 'orange': 4}

merged = {}

for key, value in d1.items():
  if key not in merged:
    merged[key] = value

for key, value in d2.items():
  if key in merged:
    merged[key] += value
  else :
    merged[key] = value

print(merged)


# Q4. Find the key with the highest value
# Return the key with the largest numeric value. If multiple keys tie, return the first such key in insertion order.
# Expected input: {'A': 82, 'B': 95, 'C': 91, 'D': 95}
# Expected output: 'B'

d =  {'A': 82, 'B': 95, 'C': 91, 'D': 95}

max = float('-inf')

for key, value in d.items():
  if d[key] > max:
    max = d[key]
for key, value in d.items():
  if value == max:
    print(key)
    break


# Q5. Group words by their first letter
# Create a dictionary where each lowercase first letter maps to a list of words beginning with that letter. Keep input order.
# Expected input: ["apple", "ant", "banana", "boat", "avocado"]
# Expected output: {'a': ['apple', 'ant', 'avocado'], 'b': ['banana', 'boat']}

input = ["apple", "ant", "banana", "boat", "avocado"]
words = set([w[0] for w in input])
merged = {}
for items in input:
  for key in words:
    if items[0] == key:
      if key not in merged:
        merged[key] = [items]
      else :
        merged[key].append(items)
print(merged)



# Q6. Create a dictionary from two lists
# Given equal-length lists of keys and values, create a dictionary. If a key repeats, the last value should win.
# Expected input: keys = ['x', 'y', 'x', 'z'], values = [1, 2, 3, 4]
# Expected output: {'x': 3, 'y': 2, 'z': 4}

keys = ['x', 'y', 'x', 'z']
values = [1, 2, 3, 4]
merged = {}
for i, j in zip(reversed(keys),reversed(values)):
  if i not in merged:
      merged[i] = j
print(merged)

#dict coding questions
# Q9. Find keys with matching values
# Return a list of keys whose values are equal in both dictionaries. Only keys present in both dictionaries can be returned.
# Expected input: d1 = {'a': 10, 'b': 20, 'c': 30, 'd': 40}, d2 = {'a': 10, 'b': 25, 'c': 30, 'e': 50}
# Expected output: ['a', 'c']

d1 = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
d2 = {'a': 10, 'b': 25, 'c': 30, 'e': 50}
l=[]
common_key = d1.keys() & d2.keys()


for key in common_key:
  if d1[key]==d2[key]:
    l.append(key)
print(l)



# Q7. Filter dictionary entries by threshold
# Return a new dictionary containing only entries whose numeric value is greater than or equal to the threshold.
# Expected input: scores = {'A': 67, 'B': 88, 'C': 72, 'D': 91}, threshold = 75

scores = {'A': 67, 'B': 88, 'C': 72, 'D': 91}
threshold = 75
result = []
for key, value in scores.items():
  if value >= threshold:
    result.append(key)
print(result)



# Q7. Filter dictionary entries by threshold
# Return a new dictionary containing only entries whose numeric value is greater than or equal to the threshold.
# Expected input: scores = {'A': 67, 'B': 88, 'C': 72, 'D': 91}, threshold = 75

scores = {'A': 67, 'B': 88, 'C': 72, 'D': 91}
threshold = 75
result = {}
for key, value in scores.items():
  if value >= threshold:
    result[key] = value
print(result)



# Calculate total sales by product
# Given a list of transactions, sum the quantity for each product and return a dictionary of product totals.
# Expected input: [('pen', 3), ('book', 2), ('pen', 4), ('pencil', 5), ('book', 1)]
# Expected output: {'pen': 7, 'book': 3, 'pencil': 5}

input = [('pen', 3), ('book', 2), ('pen', 4), ('pencil', 5), ('book', 1)]
d = {}
for name, count in input:
    if name not in d:
      d[name] = count
    else :
      d[name]+= count
print(d)