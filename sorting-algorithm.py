
def total_sort(shorting_algorithm, arr):
    return shorting_algorithm(arr)
    

    
def __init__(self, arr) -> None:
    self.arr = arr

'''Bubble sort: bubble sort repeatidly steps through the list, compares adjacent elements, and swap them if they are in the wrong order. It continues until the list is sorted.'''

'''The time complexity of Bubble Sort is O(n^2) in the worst and average cases, where n is the number of elements in the array. This makes it inefficient for the large array, and it generally not used in practice for sorting large dataset'''

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
    
'''Selection sort works by dividing the input array into two parts. The sorted sublist at the begining and the unsorted sublists at the end. it repeatidely finds the minimum element from the unsorted sublist and swap it with the left most unsorted element, thus expanding the sorted sublist by one element'''

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
            
    return arr

'''Quick sort is a popular sorting algorithm known for it efficiency and versatility. It follows the divide and conquer approach, which means it divides the array into smaller sub-array independently and then combines them to form a sorted array
steps
1. choose a pivot
2. Partioning: 
3. recursively sort sub-array
4. combine
'''

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)
    
'''Insertion sort algorithm is a simple and efficient sorting algorithm that builds the final sorted array one at a time. It is perticularly used for small detasets or nearly sorted datasets
Steps:
1. Start from the second element of the array, assuming the first element is already sorted
2. Compare and insert
3. Repeat'''

def insertion_Sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


'''
    Merge Sort divide and conquer paradigm
    It divides the input array into two halves, sort each halves recursively and then merges the sorted halves to produce a sorted output.
'''

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        # recurisevely divide arr until we left with a singal index
        merge_sort(left)
        merge_sort(right)
        
        i = j =  k = 0  # Initialize pointers for the left, right, and merged arrays
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            
        
        # Check if any elements are remaining in the left or right halves
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr
        
        




arr = [4, 2, 3, 1, 5]
result = total_sort(merge_sort, arr)
print(result)



