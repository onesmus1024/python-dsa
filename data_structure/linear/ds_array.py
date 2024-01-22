import array


# creating an array with integer type
arr = array.array('i', [1, 2, 3, 4, 5])

# traverse the array

for i in range(len(arr)):
    print(arr[i], end=' ')
    

# sort the array
arr = array.array('i', [1, 2, 3, 4, 5])
arr.reverse()
print(arr)


# insert the element in the array
arr = array.array('i', [1, 2, 3, 4, 5])
arr.insert(1, 6)
print(arr)

# delete the element in the array
arr = array.array('i', [1, 2, 3, 4, 5])
arr.remove(5)
print(arr)

# search the element in the array
arr = array.array('i', [1, 2, 3, 4, 5])
print(arr.index(3))

# update the element in the array
arr = array.array('i', [1, 2, 3, 4, 5])
arr[2] = 6
print(arr)

# find the length of the array
arr = array.array('i', [1, 2, 3, 4, 5])
print(len(arr))

# find the maximum element in the array
arr = array.array('i', [1, 2, 3, 4, 5])
print(max(arr))

# find the minimum element in the array
arr = array.array('i', [1, 2, 3, 4, 5])
print(min(arr))

# find the sum of the element in the array
arr = array.array('i', [1, 2, 3, 4, 5])
print(sum(arr))

# find the average of the element in the array
arr = array.array('i', [1, 2, 3, 4, 5])
print(sum(arr)/len(arr))






