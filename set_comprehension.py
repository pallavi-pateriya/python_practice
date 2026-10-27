# 1. Create a set of unique numbers.
numbers = [1, 2, 2, 3, 3, 4, 5, 5]
s={i for i in numbers}
print(s)

# 2. Create a set containing only even numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
s={i for i in numbers if i%2==0}
print(s)

# 3. Create a set containing the squares of all numbers. Duplicate results should be removed.
numbers = [1, 2, 2, 3, 3, 4]

s= {i**2 for i in numbers}
print(s)

# 4. Create a set containing the lengths of all words. Duplicate lengths should appear only once.
words = ['apple', 'banana', 'kiwi', 'cat']
s={len(i) for i in words}
print(s)

# 5. Create a set of absolute values.
numbers = [-1, -2, 2, 3, -3, 4,-8]
s={abs(i) for i in numbers}
print(s)

# 6. Select numbers greater than 15 and store them in a set.
numbers = [5, 10, 15, 20, 25, 30]
s={i for i in numbers if i > 15}
print(s)

# 7. Create a set of uppercase words. Duplicate words should be removed.
words = ['python', 'django', 'python', 'fastapi']

s={i.upper() for i in words}
print(s)

# 8. Create a set containing the cubes of odd numbers only.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s={i**3 for i in numbers if i%2!=0}
print(s)

# 9. Create a set of elements that exist in both lists a and b.
a = [1, 2, 3, 4,10]
b = [3, 4,10,5, 6]
s={i for i in a for j in b if i==j}
print(s)

# 10. Create a set of unique words whose length is at least 4.
words = ['cat', 'dog', 'elephant', 'ant', 'tiger', 'cat']
s={word for word in words if len(word)>=4}
print(s)