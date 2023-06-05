# Naive solution

def naive_two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None

# Hashmap solution

def two_sum(nums, target):
    map = {}

    # track both index and value of nums
    for i, num in enumerate(nums):
        # find difference between target and value
        # if it's in the hashmap then return the index of it
        diff = target - num
        if diff in map:
            return [map[diff], i]
        
        # otherwise just add it to hashmap
        map[num] = i
    return None