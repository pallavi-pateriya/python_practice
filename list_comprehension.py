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

