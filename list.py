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