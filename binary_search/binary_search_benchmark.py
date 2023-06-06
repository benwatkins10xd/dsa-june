import timeit
import time
import gc
import os
import random
import matplotlib.pyplot as plt

times = []

'''
This will benchmark the solutions to binary search

Timing in python can give results with high variations. This is due to:
- garbage collection
- other processes using resources
- processes taking priority

So we'll disable GC and set process priority to high below.
'''

# disable garbage collection
gc.disable()

# set process priority to high, Windows only
if os.name == 'nt':
    import psutil
    psutil.Process(os.getpid()).nice(psutil.HIGH_PRIORITY_CLASS)
from typing import List

# Naive solution
def naive_solution(nums: List[int], target: int) -> int:
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        else:
            return -1
        
# Proper solution
def binary_search(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def benchmark_binary_search(array):
    # take an array and use the middle + 4'th element as the target
    if len(array) % 2 == 0:
        middle = len(array) // 2 - 1
        target = array[middle + 4]
    else:
        middle = len(array) // 2
        target = array[middle + 4]

    def wrapper():
        naive_solution(array, target)
    # Measure the execution time of the binary search function
    execution_time = timeit.timeit(wrapper, number=1)
    # times.append(execution_time)
    print(f"Array length: {len(array)}\tExecution time: {execution_time:.6f} seconds")


# Define different array lengths
array_lengths = [10000000, 20000000, 30000000, 50000000, 100000000, 200000000]
arrays = []
for i in array_lengths:
    arrays.append(list(range(i)))

times = [i * 0.00000004 for i in array_lengths]

# Run the benchmark
for array in arrays:
    benchmark_binary_search(array)

plt.plot(array_lengths, times, "+", markersize=8)
plt.xlabel("String length")
plt.ylabel("Time (seconds)")
plt.savefig(f'{time.time()}.png')
print(f"Created {time.time()}.png")


