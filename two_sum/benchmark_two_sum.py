import timeit
import time
import gc
import os
import random
import matplotlib.pyplot as plt

times = []

'''
This will benchmark the solutions to two sum.

Timing in python can give results with high variations. This is due to:
- garbage collection
- other processes using resources
- processes taking priority

So we'll disable GC and set process priority to high below.
'''

# disable garbage collection
gc.disable()

# set process priority to high
if os.name == 'nt':
    import psutil
    psutil.Process(os.getpid()).nice(psutil.HIGH_PRIORITY_CLASS)

class Solution:
    def naive_two_sum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return None

# Benchmark function
def benchmark_two_sum(array_size):
    nums = [random.randint(1, 100) for _ in range(array_size)]
    target = random.randint(1, 200)
    
    def wrapper():
        sol = Solution()
        # change this for naive/optimised
        sol.naive_two_sum(nums, target)
    
    duration = timeit.timeit(wrapper, number=10000)  # Perform 10,000 iterations
    times.append(duration)
    print(f"Benchmark for array size {array_size}: {duration:.6f} seconds")

# Test different array sizes
array_sizes = [10, 100, 1000, 3000, 6000, 8000, 10000]

for size in array_sizes:
    benchmark_two_sum(size)

plt.plot(array_sizes, times, "+", markersize=8)
plt.xlabel("Array size")
plt.ylabel("Time (seconds)")
plt.savefig(f'{time.time()}.png')
print(f"Created {time.time()}.png")


