'''In DSA, searching algorithms are used to find a particular element within a collection of element such as array, LinkedList or Tree.
There are various types of searching algorithm such as Linear search, Binary search, HAshing.
'''


def total_search(search_algorithm, *args):
    return search_algorithm(*args)


# Linear search:
'''Linear search is a simplest searching algorithm that sequentially checks each element of the collection until the match is found or the entire collection has been traversed'''

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Binary search:
'''Binary search is a more efficient algorithm, but it requires the collection to be sorted. It works repeatidely dividing in half portion of the collection, until the possible location for the item are narrowed down to one.'''

def binary_Search(arr, x):
    low = 0          # [1, 2, 3, 4, 5], mid = 2
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            if arr[mid] > x:
                low -= 1    
    return -1    


# Hashing:
'''Hashing often involves the use of hash table, where the key is hashed to determine its index in the table '''
def hash_search(hash_table, key):
    for h_key in hash_table:
        if h_key == key:
            return hash_table[h_key]
    return -1




        

array = [1, 3, 5, 8, 12, 17]
hash = {
    "1": "Rahul",
    "2": "Dheeraj",
    "3": "Angela"
}
dict = {}
result = total_search(hash_search, hash, "3")
# result = hash_search("3", hash)
print(result)    

