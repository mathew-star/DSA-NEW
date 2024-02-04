"""
this is insertion sort>>
Insertion sort takes the maximum time to sort if elements are sorted in reverse order. And it takes minimum time (Order of n) when elements are already sorted.
Insertion sort is used when number of elements is small. It can also be useful when the input array is almost sorted, and only a few elements are misplaced in a complete big array.

The worst-case time complexity of the Insertion sort is O(N^2)
The average case time complexity of the Insertion sort is O(N^2)
The time complexity of the best case is O(N).
"""

nums=[0,9,4,6,4,2]

for i,n in enumerate(nums):
    current=i
    while current>0 and nums[current]<nums[current-1]:
        nums[current],nums[current-1]=nums[current-1],nums[current]
        current -= 1
print(nums)


"""
Program to sort recursively>>>> 
"""
def recursive_insertion_sort(arr, n):
    # Base case: If the array has only one element, it is already sorted
    if n <= 1:
        return

    # Recursively sort the first n-1 elements
    recursive_insertion_sort(arr, n-1)

    # Insert the last element into its correct position in the sorted part
    key = arr[n-1]
    j = n-2

    # Move elements greater than key to one position ahead of their current position
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    # Insert the key into its correct position
    arr[j + 1] = key

# Example usage:
my_array = [12, 11, 13, 5, 6]
recursive_insertion_sort(my_array, len(my_array))

print("Sorted array:", my_array)
