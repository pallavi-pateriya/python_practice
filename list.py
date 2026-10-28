#list coding questions
#Remove duplicates while preserving order
# Expected output: [4, 2, 3, 1]

input = [4, 2, 4, 3, 2, 1, 3]

def func(input):
    output = []
    for i in input:
        if i not in output:
            output.append(i)
    return output
print(func(input))


# Return the second-largest distinct value in a list. Assume at least two distinct values exist.
input =[10, 5, 8, 10, 7, 8]
# Expected output: 8
max_value = float('-inf')
sec_value = float('-inf')

#min_value = float('inf')

for i in input:
  if i > max_value:
    sec_value = max_value
    max_value = i
  elif i < max_value and i > sec_value:
      sec_value = i
print(sec_value)


#Move all zeros to the end

input = [0, 5, 0, 3, 8, 0, 2]

input = [0, 5, 0, 3, 8, 0, 2]
l = len(input)
c = 0
for i in input:
    if i == 0:
        input.remove(i)
        c+= 1
while c:
    input.append(0)
    c-= 1
print(input)


# Rotate a list to the right by k positions. Handle k values larger than the list length.
# Expected input: list = [1, 2, 3, 4, 5], k = 2
# Expected output: [4, 5, 1, 2, 3]


list = [1, 2, 3, 4, 5]
k = 2
k = k % len(list)
rotated = list[-k:] + list[:-k]
print(rotated)  


# Q5. Find pairs with a target sum
# Return all unique pairs of numbers whose sum equals the target. Each pair should be in ascending order, and pairs should not
# repeat.
# Expected input: numbers = [1, 5, 7, -1, 5, 3], target = 6
# Expected output: [[-1, 7], [1, 5]]


input = [1, 5, 7, -1, 5, 3]
target = 6
l1 = set()

for i in range(len(input)):
  for j in range(i+1, len(input)):
    if input[i]+input[j] == target:
      pair =tuple(sorted([input[i],input[j]]))
      l1.add(pair)
print(l1)


# Q5. Find pairs with a target sum
# Return all unique pairs of numbers whose sum equals the target. Each pair should be in ascending order, and pairs should not
# repeat.
# Expected input: numbers = [1, 5, 7, -1, 5, 3], target = 6
# Expected output: [[-1, 7], [1, 5]]


input_list = [1, 5, 7, -1, 5, 3]
target = 6
l1 = []

for i in range(len(input_list)):
  for j in range(i+1, len(input_list)):
    if input_list[i] + input_list[j] == target:
      pair = sorted([input_list[i], input_list[j]])
      
      if pair not in l1:
        l1.append(pair)

l1.sort()
print(l1)


# Q6. Flatten a one-level nested list
# Convert a list containing integers and lists of integers into one flat list. Only one level of nesting is present.
# Expected input: [1, [2, 3], 4, [5, 6, 7]]


input = [1, [2, 3], 4, [5, 6, 7]]

a = []
for i in input:
    if type(i) == int:
        a.append(i)
    elif type(i) == list:
        for j in i:
            a.append(j)
print(a)

#using isinstance to find the type of element
flattened = []
for x in input:
    if isinstance(x, list):
        for j in x:
            flattened.append(j)
    else:
        flattened.append(x)

print(flattened)

# Q7. Split a list into chunks
# Split a list into consecutive chunks of size n. The final chunk may contain fewer than n elements.
# Expected input: values = [1, 2, 3, 4, 5, 6, 7], n = 3
# Expected output: [[1, 2, 3], [4, 5, 6], [7]]

values = [1, 2, 3, 4, 5, 6, 7]
n = 3
# Expected output: [[1, 2, 3], [4, 5, 6], [7]]
l1=[]
for i in range(0,len(values),n):
  chunk = values[i:i+n]
  l1.append(chunk)
print(l1)

l=[values[i:i+n] for i in range(0,len(values),n)]
print(l)



# Q9. Merge two sorted lists
# Merge two ascending-sorted lists into one ascending-sorted list without calling sort() or sorted().
# Expected input: a = [1, 4, 7, 9], b = [2, 3, 7, 10]
# Expected output: [1, 2, 3, 4, 7, 7, 9, 10]
a = [1, 4, 7, 9]
b = [2, 3, 7, 10]

def func(a, b):
    result = []
    i, j = 0, 0
    
    while i < len(a) and j < len(b):
      if a[i] <= b[j]:
            result.append(a[i])
            i += 1
      else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    
    return result

print(func(a, b))



# Q10. Find elements common to three lists
# Return distinct elements that occur in all three lists, ordered by their first appearance in the first list.
# Expected input: a = [5, 2, 8, 2, 9, 1], b = [2, 5, 7, 8], c = [8, 2, 5, 5]
# Expected output: [5, 2, 8]

a = [5, 2, 8, 2, 9, 1]
b = [2, 5, 7, 8]
c = [8, 2, 5, 5]

result = []
for item in a:
  if item in b and item in c and item not in result:
    result.append(item)
print(result)





# Return the longest strictly increasing contiguous sublist. If there is a tie, return the first such run.
# Expected input: [1, 2, 2, 3, 4, 1, 2, 3]
# Expected output: [2, 3, 4]
  