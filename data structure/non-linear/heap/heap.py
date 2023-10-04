# Max-Heap data structure in Python

class MaxHeap:
    def __init__(self):
        self.arr = []

    def heapify(self, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2 
    
        if l < n and self.arr[i] < self.arr[l]:
            largest = l
    
        if r < n and self.arr[largest] < self.arr[r]:
            largest = r
    
        if largest != i:
            self.arr[i],self.arr[largest] = self.arr[largest],self.arr[i]
            self.heapify(n, largest)

    def insert(self, newNum):
        size = len(self.arr)
        if size == 0:
            self.arr.append(newNum)
        else:
            self.arr.append(newNum);
            for i in range((size//2)-1, -1, -1):
                self.heapify(size, i)

    def deleteNode(self, num):
        size = len(self.arr)
        i = 0
        for i in range(0, size):
            if num == self.arr[i]:
                break
        
        self.arr[i], self.arr[size-1] = self.arr[size-1], self.arr[i]

        self.arr.remove(num)
        
        for i in range((len(self.arr)//2)-1, -1, -1):
            self.heapify(len(self.arr), i)
    
    def __str__(self):
        return "Max-Heap array: " + str(self.arr)

heap = MaxHeap()
heap.insert(3)
heap.insert(4)
heap.insert(9)
heap.insert(5)
heap.insert(2)

print(heap)

heap.deleteNode(4)
print("After deleting an element: " + str(heap))
