# Return values that appear in exactly one of the two sets.
# Expected input: A = {1, 2, 3, 4}, B = {3, 4, 5, 6}
# Expected output: {1, 2, 5, 6}

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A = A.union(B)
print(A)

# Check whether one set is a proper subset
# Return True if A is a subset of B and A is not equal to B; otherwise return False.
# Expected input: A = {2, 4}, B = {2, 4, 6}

A = {2, 4}
B = {2, 4, 6}

is_subset = True
for item in A:
  if item not in B:
    is_subset = False
 
if is_subset:
  print(True)
else:
  print(False)


# Given three sets of attendee IDs, return the IDs present in all three events.
# Expected input: 
event1 = {101, 102, 103, 105}
event2 = {102, 103, 104}
event3 = {102, 103, 106}
#Expected output: {102, 103}
a=set()
for i in event1:
  if i in event2 and i in event3:
    a.add(i)
print(a)

# Q4. Remove banned values
# Remove every value in the banned set from the input set.
# Expected input: values = {10, 20, 30, 40, 50}, banned = {20, 50, 70}
# Expected output: {10, 30, 40}

values = {10, 20, 30, 40, 50}
banned = {20, 50, 70}

for item in list(values):
  if item in banned:
    values.remove(item)
print(values)

# Q5. Count distinct words across two sentences
# Convert both sentences to lowercase, split on whitespace, and return the number of distinct words across both sentences.
# Markdown Live Preview https://markdownlivepreview.com/2 of 5 23/10/26, 11:00
# Expected input: sentence1 = "Python is Easy", sentence2 = "easy coding with Python"
# Expected output: 5

sentence1 = "Python is Easy"
sentence2 = "easy coding with Python"


sentence1 = sentence1.lower().split()
sentence2 = sentence2.lower().split()
a = set(sentence1)
b = set(sentence2)
print(a)
print(b)
a = a.union(b)
print(len(a))



# Find missing numbers in a range
# Given a list containing unique integers from 1 through n with some values missing, return the missing values as a set.
# Expected input: values = [1, 2, 5, 7], n = 8
# Expected output: {3, 4, 6, 8}

values = [1, 2, 5, 7]
n = 8

min = float('+inf')
for i in values:
  if i < min:
    min=i
a = set()
for i in range(min,n+1):
  if i not in values:
    a.add(i)
print(a)

# Check if two lists contain the same unique values
# Return True if both lists have the same set of values, regardless of order or repeated occurrences.
# Expected input: a = [1, 2, 2, 3, 4], b = [4, 3, 2, 1, 1]
# Expected output: True

a = [1, 2, 2, 3, 4]
b = [4, 3, 2, 1, 1]
a= set(a)
b=set(b)
for item in a: 
  if item in b:
    similar= True
  else :
    similar = False

print(similar)

# Q8. Find values exclusive to each group
# Given sets A and B, return a pair of sets: values only in A and values only in B.
# Expected input: A = {1, 2, 3, 7}, B = {3, 4, 5, 7}
# Expected output: ({1, 2}, {4, 5})


A = {1, 2, 3, 7}
B = {3, 4, 5, 7}
sub1 = set()
sub2 = set()
for item in A:
  if item not in B:
    sub1.add(item)
for item in B:
  if item not in A:
    sub2.add(item)
print(f"{{ {sub1}, {sub2} }}")


# Q9. Check whether two lists are disjoint
# Return True if the lists have no values in common; otherwise return False. Use sets to solve it.
# Expected input: a = [1, 3, 5, 7], b = [2, 4, 6, 8, 5]
# Expected output: False




a = [1, 3, 5, 7]
b = [2, 4, 6, 8, 5]
c = a+b
a = set(a)
b = set(b)

a = a.union(b)
if len(a) < len(c):
  print(False)
else :
  print(True)

# Find the union of multiple sets
# Given a list of sets, return one set containing every distinct value found in any set.
# Expected input: [{1, 2}, {2, 3, 4}, {4, 5}, {1, 6}]
# Expected output: {1, 2, 3, 4, 5, 6}


input = [{1, 2}, {2, 3, 4}, {4, 5}, {1, 6},{9}]
a = set()
for item in input:
  for i in item:
    a.add(i)
print(a)


# Q1. Count the frequency of each item
# Build a dictionary mapping each item to the number of times it appears. The order of keys does not matter.
# Expected input: ["apple", "banana", "apple", "orange", "banana", "apple"]
# Expected output: {"apple": 3, "banana": 2, "orange": 1}




input = ["apple", "banana", "apple", "orange", "banana", "apple"]

output = {}

for item in input:
  if item in output:
    output[item]+=1
  else :
    output[item]=1
print(output)


# Q2. Invert a dictionary with duplicate values
# Invert a dictionary so each original value maps to a list of all keys that had that value.
# Expected input: {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
# Expected output: {1: ['a', 'c'], 2: ['b', 'e'], 3: ['d']}


input = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}

d={}

for key, value in input.items():
  if value in d:
    d[value].append(key)
  else:
    d[value] = [key]
print(d)

# Q3. Merge dictionaries by summing common keys
# Merge two dictionaries. If a key appears in both, add the values; otherwise keep the available value.
# Expected input: d1 = {'apple': 3, 'banana': 2}, d2 = {'banana': 5, 'orange': 4}
# Expected output: {'apple': 3, 'banana': 7, 'orange': 4}



d1 = {'apple': 3, 'banana': 2}
d2 = {'banana': 5, 'orange': 4}

combined = {}

for key , value in d1.items():
  combined[key]=value

for key, value in d2.items():
  if key in combined:
    combined[key]+=value
  else :
    combined[key] = value
print(combined)




# Return the key with the largest numeric value. If multiple keys tie, return the first such key in insertion order.
# Expected input: {'A': 82, 'B': 95, 'C': 91, 'D': 95}
# Expected output: 'B'


input = {'A': 82, 'B': 100, 'C': 91, 'D': 100}

max = float('-inf')
found = ""
for key, value in input.items():
  if value > max:
    max = value
for key, value in input.items():
  if value == max:
    found = key
    break
print(found)



# Create a dictionary where each lowercase first letter maps to a list of words beginning with that letter. Keep input order.
# Expected input: ["apple", "ant", "banana", "boat", "avocado"]
# Expected output: {'a': ['apple', 'ant', 'avocado'], 'b': ['banana', 'boat']}

word_list= ["apple", "ant", "banana", "boat", "avocado"]

a = {}

for word in word_list:
    key = word[0] 
    if key not in a:
        a[key] = []
    a[key].append(word)

print(a)


# Given equal-length lists of keys and values, create a dictionary. If a key repeats, the last value should win.
# Expected input: keys = ['x', 'y', 'x', 'z'], values = [1, 2, 3, 4]
# Expected output: {'x': 3, 'y': 2, 'z': 4}
keys = ['x', 'y', 'x', 'z']
values = [1, 2, 3, 4]
a={}


for key, value in zip(reversed(keys), reversed(values)):
  if key not in a:
    a[key] = value
print(a)


# Filter dictionary entries by threshold
# Return a new dictionary containing only entries whose numeric value is greater than or equal to the threshold.
# Expected input: scores = {'A': 67, 'B': 88, 'C': 72, 'D': 91}, threshold = 75
# Expected output: {'B': 88, 'D': 91}

scores = {'A': 67, 'B': 88, 'C': 72, 'D': 91}
threshold = 75
a = {}

for key, value in scores.items():
  if value > threshold:
    a[key]=value
print(a)


# Given a list of transactions, sum the quantity for each product and return a dictionary of product totals.
# Expected input: [('pen', 3), ('book', 2), ('pen', 4), ('pencil', 5), ('book', 1)]
# Expected output: {'pen': 7, 'book': 3, 'pencil': 5}

input = [('pen', 3), ('book', 2), ('pen', 4), ('pencil', 5), ('book', 1)]
a={}
for i in input:
 if i[0] not in a:
   a[i[0]] = i[1]
 else :
  a[i[0]]+= i[1]
print(a)

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

