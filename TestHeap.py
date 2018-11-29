from Lab5 import Heap
from Lab5 import heap_sort

# heap to populate
heap = Heap()

# hard coded list of values
list = [5, 2, 6, 8, 2, 4, 7, 3, 4, 1, 2, 9, 5, 6, 0]

# populate the heap
for elem in list:
    heap.insert(elem)

# apply heapsort to the heap and return the sorted array
result = heap_sort(list)

# print the values in the sorted array
for i in result:
    print(i)
