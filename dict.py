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