# for, for-else, while, while-else
# continue, break

# l = [10, 20, 30, "abcd", False, "abcde"]

# find the first string element inside the given list
# find elements that are integers and add 10 to them inside the given list
# loop variable or iterable
# for ele in l:
#     if type(ele) == int:
#         print(ele + 10)
#         continue
#     if type(ele) == str:
#         print(ele)
#         # break
#     print("I am outside if block")
# else:
#     print("I am outside for loop and loop got exited without any break statement")

# l = [10, 20, 30, "abcd", False, "abcde"]
# l = [False, True, [1, 2, 3]]

# idx = 0

# while idx < len(l):
#     ele = l[idx]
#     if type(ele) == int:
#         print(ele + 10)
#         # idx = idx + 1
#         idx += 1
#         continue
#     if type(ele) == str:
#         print(ele)
#         break
#     print("I am outside if block")
#     idx += 1
# else:
#     print("I am outside loop and loop got exited without any break statement")

# d = {'k': 123, (1, 2, 3, 4): 123, (1, 2, 3, 4, 5): list(str(123))}
# for k, v in d.items():
#     print(k, v)

l = (10, 20, 30, "abcd", False, "abcde")
# for idx, ele in enumerate(l):
#     print(idx, ele)

print(list(range(len(l))))

for idx in range(len(l)):
    print(l[idx])