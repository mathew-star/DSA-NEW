"""
Selection sort is a simple and efficient sorting algorithm that works by 
repeatedly selecting the smallest (or largest) element from the unsorted portion of the 
list and moving it to the sorted portion of the list.

Advantages of Selection Sort Algorithm

Simple and easy to understand.
Works well with small datasets.

Disadvantages of the Selection Sort Algorithm

Selection sort has a time complexity of O(n^2) in the worst and average case.
Does not work well on large datasets.
Does not preserve the relative order of items with equal keys which means it is not stable.


"""
nums=[1,3,4,2,5,9,6]
for i in range(len(nums)):
    min_indx=i
    for j in range(i+1, len(nums)):
        if nums[min_indx]>nums[j]:
            min_indx=j
    nums[i],nums[min_indx]=nums[min_indx],nums[i]
print(nums)