"""
Time Complexity: O(N2)
Auxiliary Space: O(1)

Advantages of Bubble Sort:
Bubble sort is easy to understand and implement.
It does not require any additional memory space.
It is a stable sorting algorithm, meaning that elements with the same key value maintain their relative order in the sorted output.

Disadvantages of Bubble Sort:
Bubble sort has a time complexity of O(N2) which makes it very slow for large data sets.
Bubble sort is a comparison-based sorting algorithm, which means that it requires a comparison operator to determine the relative order of elements in the input data set.
 It can limit the efficiency of the algorithm in certain cases.
"""


nums=[1,9,6,4,2,8]
for i in range(len(nums)):
    swapped=False
    for j in range(0,len(nums)-i-1):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
            swapped=True
    if swapped == False:
        break

print(nums)

"""
Bubble sort using recursion>>>>
"""
def bubble_sort_recursive(arr, n):
    # Base case: If the entire list is traversed without any swaps, it's sorted
    if n == 1:
        return

    # One pass through the list to move the largest element to the end
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            # Swap elements if they are in the wrong order
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    # Recursive call for the remaining elements
    bubble_sort_recursive(arr, n - 1)

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)

bubble_sort_recursive(arr, n)

print("Sorted array:", arr)
