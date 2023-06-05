import time
import random
import matplotlib.pyplot as plt

times = []

def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None

def generate_large_list(size):
    return [random.randint(-1000, 1000) for _ in range(size)]

def time_two_sum(array_sizes):
    for size in array_sizes:
        nums = generate_large_list(size)
        target = random.randint(-2000, 2000)

        start_time = time.perf_counter()
        print(start_time)
        two_sum(nums, target)
        end_time = time.perf_counter()

        time_taken = end_time - start_time
        times.append(time_taken)
        print(f"Array Size: {size}, Time Taken: {time_taken} seconds")

# Example usage:
array_sizes = [100000, 1000000, 10000000]
time_two_sum(array_sizes)

plt.plot(array_sizes, times)
plt.show()