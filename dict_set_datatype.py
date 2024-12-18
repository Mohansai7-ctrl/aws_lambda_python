# d = {'k': 123, (1, 2, 3, 4): 123, (1, 2, 3, 4, 5): list(str(123))}
# print(d[(1, 2, 3, 4, 5)])
# print(dir(d))

"""
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
"""
# print(d.keys())
# print(d.values())
# print(d.items())
# [('k', 123), ((1, 2, 3, 4), 123), ((1, 2, 3, 4, 5), ['1', '2', '3'])]
# A dict is a mutable datatype

# d['k'] = 1234
# print(d)

# Set
s = {'a', 'a', 'b', 'c'}
# print(s)
# {'b', 'a', 'c'}
# s[0] = 'abc' # TypeError: 'set' object does not support item assignment
# print(dir(s))

"""
'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'
"""

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
print("bananaa" in thisset)
print("banana" not in thisset)