from typing import List

# Naive solution
def naive_solution(nums: List(int), target: int) -> int:
    # Just go through every element in the list and see if we get a match
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        else:
            return -1
        
# Proper solution
def binary_search(nums: List(int), target: int) -> int:
    # lower and upper pointers of search
    low = 0
    high = len(nums) - 1

    # search while the low pointer is <= high pointer
    while low <= high:
        # finds middle of nums array
        mid = (low + high) // 2 # // denotes floor division
        # if middle value = target then we're done
        if nums[mid] == target:
            return mid
        # if we're below the target, search in upper section of array
        elif nums[mid] < target:
            low = mid + 1
        # otherwise search in lower section
        else:
            high = mid - 1

    return -1