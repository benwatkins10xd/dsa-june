import timeit
import time
import gc
import os
import random
import matplotlib.pyplot as plt

times = []

'''
This will benchmark the solutions to is anagram

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

def naive_is_anagram(s: str, t: str) -> bool:    
    if len(s) != len(t):
        return False
    
    str1_list = list(s)
    str2_list = list(t)
    
    str1_list.sort()
    str2_list.sort()
    
    for i in range(len(str1_list)):
        if str1_list[i] != str2_list[i]:
            return False
    
    return True

# Hashmapped solution
def faster_is_anagram(s: str, t: str) -> bool:
    sMap = {}
    tMap = {}

    for i in s:
        sMap[i] = sMap.get(i, 0) + 1
    
    for i in t:
        tMap[i] = tMap.get(i, 0) + 1

    if sMap == tMap:
        return True
    else:
        return False

def benchmark_anagram_checker(string_size):
    str1 = "abcdefg" * string_size
    str2 = "bcdefga" * string_size

    def wrapper():
        naive_is_anagram(str1, str2)
    # Measure the execution time of the anagram checker function
    execution_time = timeit.timeit(wrapper, number=1)
    times.append(execution_time)
    print(f"String length: {string_size}\tExecution time: {execution_time:.6f} seconds")


# Define different string lengths
string_lengths = [1000, 10000, 100000, 300000, 600000, 1000000, 3000000, 7000000, 10000000]

# Run the benchmark
for size in string_lengths:
    benchmark_anagram_checker(size)

plt.plot(string_lengths, times, "+", markersize=8)
plt.xlabel("String length")
plt.ylabel("Time (seconds)")
plt.savefig(f'{time.time()}.png')
print(f"Created {time.time()}.png")


