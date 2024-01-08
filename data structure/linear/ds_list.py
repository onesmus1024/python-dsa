

list_1 = list([1, 2, 3, 4, 5])

# traverse the list

for i in range(len(list_1)):
    print(list_1[i], end=' ')

# sort the list

list_1.reverse()
print(list_1)

# insert the element in the list

list_1.insert(1, 6)

print(list_1)

# delete the element in the list

list_1.remove(5)

print(list_1)

# search the element in the list

print(list_1.index(3))

# update the element in the list

list_1[2] = 6

print(list_1)

# find the length of the list

print(len(list_1))

# find the maximum element in the list

print(max(list_1))

# find the minimum element in the list

print(min(list_1))

