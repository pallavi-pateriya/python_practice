# 1. Create a list of squares of numbers from 1 to 10.
l=[i**2 for i in range(1,11)]
print(l)


# 2. Given numbers = [1, 2, 3, 4, 5, 6, 7, 8], create a list containing only even numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
l=[i for i in numbers if i%2==0]
print(l)


# 3. Given numbers = [1, 2, 3, 4, 5, 6, 7, 8], create a list containing only odd numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

l=[i for i in numbers if i%2!=0]
print(l)

# 4. Convert every string in names = ['monika', 'rahul', 'priya'] to uppercase.

names = ['monika', 'rahul', 'priya']
l=[i.upper() for i in names]
print(l)

# 5. Given numbers = [10, 20, 30, 40, 50], create a list where every number is increased by 5.

numbers = [10, 20, 30, 40, 50]
l=[i+5 for i in numbers]
print(l)

# 6. From numbers = [12, 5, 23, 8, 40, 15, 3], select numbers greater than 10.
numbers = [12, 5, 23, 8, 40, 15, 3]
l=[i for i in numbers if i > 10]
print(l)

# Given words = ['python', 'is', 'very', 'easy'], create a list containing the length of each word.

words = ['python', 'is', 'very', 'easy']

l=[len(i) for i in words]
print(l)

#8. Given numbers = [-5, 3, -2, 7, -1, 8], create a list containing the absolute value of each number.

numbers = [-5, 3, -2, 7, -1, 8]
l= [(lambda i: -i if i<0 else i) (i) for i in numbers]
print(l)


# 9. Given words = ['apple', 'cat', 'banana', 'dog', 'kiwi'], select words whose length is greater than 3.


words = ['apple', 'cat', 'banana', 'dog', 'kiwi']

l=[i for i in words if len(i)>3]
print(l)


# 10. Given numbers = [1, 2, 3, 4, 5, 6], create a list of squares of only the even numbers.

numbers = [1, 2, 3, 4, 5, 6]
l=[i**2 for i in numbers if i%2==0]
print(l)


# From the list, select numbers that are divisible by both 3 and 2, then store their squares.Given data

numbers = [2, 3, 6, 9, 12, 15, 18, 20, 24]
l=[i for i in numbers if i%2==0 and i%3==0]
print(l)


# Create a list of words that have more than 3 characters and start with a vowel (a, e, i, o, u). Convert them to uppercase.Given data

words = ['apple', 'cat', 'orange', 'elephant', 'dog', 'umbrella', 'ice', 'grapes']

l=[i.upper() for i in words if len(i)>3 and i[0] in 'aeiou']
print(l)


# 3 Flatten a nested list

# Convert the nested list into one flat list containing only numbers greater than 5.Given data

numbers = [[1, 6, 3], [8, 2, 9], [4, 7, 5]]

l=[j for i in numbers for j in i if j>5]
print(l)
