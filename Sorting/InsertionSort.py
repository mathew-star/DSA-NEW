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
    if n <= 1:
        return
    
    recursive_insertion_sort(arr, n-1)

    c=n-1

    while c > 0 and arr[c] < arr[c - 1]:

        arr[c],arr[c-1]=arr[c-1],arr[c]
        c -= 1

my_array = [12, 11, 13, 5, 6]
recursive_insertion_sort(my_array, len(my_array))

print("Sorted array:", my_array)



def recursive_selection_sort(arr, n):
    # Base case: If array has only one element, it is already sorted
    if n <= 1:
        return

    # Find the minimum element in the remaining unsorted part
    min_index = 0
    for i in range(1, n):
        if arr[i] < arr[min_index]:
            min_index = i

    # Swap the minimum element with the first element
    arr[0], arr[min_index] = arr[min_index], arr[0]

    # Recursively sort the remaining n-1 elements
    recursive_selection_sort(arr[1:], n - 1)


# Example usage:
my_array = [12, 11, 13, 5, 6]
recursive_selection_sort(my_array, len(my_array))

print("Sorted array:", my_array)