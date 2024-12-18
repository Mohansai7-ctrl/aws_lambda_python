# list

# l = [1, 2, 3, "abc", True, [10, 20, 30, "abcd", False]]
# print(l, type(l))

# l1 = l[3]
# print(l1)

# l2 = l[5][0]
# print(l2)

# l3 = l[-1][0]
# print(l3)

# print(l[len(l) - 1][0])
# print(dir(l))

"""
'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
"""

# l = [10, 20, 30, "abcd", False]

# append an element to the end of the list
# l.append(True)
# print(l)

# l.append([1, 2, 3, "abc", True])
# print(l)

# l.insert(0, "abc")
# print(l)

# res = l.insert(0, "abc")
# print(res, l)

# l = [10, 20, 30, "abcd", False]
# l.extend([1, 2, 3, "abc", True])
# print(l)

# l = [2, 3, 1]
# l.sort() # inplace
# l1 = sorted(l) # this returns a new list
# print(l, l1)

# txt = "Hello, And Welcome To My World!"
# print(txt.split(" ")

# List is a mutable datatype
l = [10, 20, 30, "abcd", False]
l[0] = 100
print(l)