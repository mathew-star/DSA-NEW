"""
Worst Case: O(N2)
Average Case: θ ( N log (N))
Best Case: Ω (N log (N))

Advantages of Quick Sort:
It is a divide-and-conquer algorithm that makes it easier to solve problems.
It is efficient on large data sets.
It has a low overhead, as it only requires a small amount of memory to function.

Disadvantages of Quick Sort:
It has a worst-case time complexity of O(N2), which occurs when the pivot is chosen poorly.
It is not a good choice for small data sets.
"""


def partition(arr, low, high):
    pivot = arr[low]
    left = low +1
    right = high
    #starting low as pivot when left > right swap low and right otherwise in high as pivot left and high
    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1

        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            break

    arr[low], arr[right] = arr[right], arr[low]
    return right

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

# Example usage:
array = [10, 7, 8, 9, 1, 5]
N = len(array)
print(array)
quicksort(array, 0, N - 1)
print(array)

###################################################################
def sort_list_interval(unsorted_list, start, end):
    # If segment is 1 or 0, it's sorted
    if end - start <= 1:
        return

    # Using first element as the pivot
    pivot = unsorted_list[start]
    start_ptr, end_ptr = start + 1, end

    # Partitioning process
    while start_ptr < end_ptr:
        # Find the next element from the left that is larger than the pivot
        while start_ptr < end_ptr and unsorted_list[start_ptr] < pivot:
            start_ptr += 1
        
        # Find the next element from the right that is smaller than or equal to the pivot
        while start_ptr < end_ptr and unsorted_list[end_ptr - 1] >= pivot:
            end_ptr -= 1

        # Swap if pointers haven't met
        if start_ptr < end_ptr:
            unsorted_list[start_ptr], unsorted_list[end_ptr - 1] = unsorted_list[end_ptr - 1], unsorted_list[start_ptr]

    # Place pivot in its final position
    unsorted_list[start], unsorted_list[start_ptr - 1] = unsorted_list[start_ptr - 1], unsorted_list[start]

    # Sort left and right of the pivot
    sort_list_interval(unsorted_list, start, start_ptr - 1)
    sort_list_interval(unsorted_list, start_ptr, end)

def sort_list(unsorted_list):
    sort_list_interval(unsorted_list, 0, len(unsorted_list))
    return unsorted_list

array = [10, 7, 8, 9, 1, 5]
res = sort_list(array)
print(res)



