import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# runtime for original code was ~ 6 seconds
# runtime complexity for original code is O(n^2)

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# runtime for new code was ~ 0.14 seconds
# runtime complexity was 
# bst = BSTNode('root')
# [bst.insert(name_1) for name_1 in names_1]
# # for name_1 in names_1: # n
# #     bst.insert(name_1) # n

# [duplicates.append(name_2) for name_2 in names_2 if bst.contains(name_2)]
# for name_2 in names_2: # n
#     if bst.contains(name_2): 
#         duplicates.append(name_2) # 1

# # O(n^2) + O(n) => n(n+1)

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# stretch
# If I had time to write it out, I would:
# Add names_1 into a list and add names_2 into a list
# Append the lists
# sort the lists
# iterate through with a list comp to and check all the instances
# where duplicates showed up and append them to duplicates

names = names_1 + names_2
names.sort()

for idx, name in enumerate(names):
    try:
        if name == names[idx + 1]:
            duplicates.append(name)
    except IndexError:
        break

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
