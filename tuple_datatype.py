# t = (1, 3, 5, "true", [10, 30, 50])
# print(t, type(t))

# t1 = t[-1]
# print(t1)

# t[0] = 100 # TypeError: 'tuple' object does not support item assignment
# Tuple is an immutable datatype
# print(dir(t))
# 'count', 'index'

# ValueError: tuple.index(x): x not in tuple
# print(t.index("abc"))
# print(t.index("true"))

# t = (1, 2, 3, 5, 1, 2, 8)
# print(t.count(1))

# unpacking
# t = (1, 2)
t = [1, 2]
# t1 = t[0]
# t2 = t[1]
t1, t2 = t
print(t1, t2)