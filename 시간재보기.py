import time
from datetime import timedelta

# print("enumerate 사용")
# start = time.process_time()

# arr = [i for i in range(10000000)]
# sum = 0

# for i, num in enumerate(arr):
#     sum += num

# end = time.process_time()

# print("Time elapsed: ", end - start)  # seconds
# print("Time elapsed: ", timedelta(seconds=end-start))

# print("------------------")
# print("enumerate 사용 X")
# start = time.process_time()

# arr = [i for i in range(10000000)]
# sum = 0

# for num in arr:
#     sum += num

# end = time.process_time()

# print("Time elapsed: ", end - start)  # seconds
# print("Time elapsed: ", timedelta(seconds=end-start))

start = time.process_time()

arr1 = [i for i in range(10000000)]
arr2 = [i for i in range(10000000, 0, -1)]
sum = 0

for i in range(10000000):
    sum += arr1[i] + arr2[i]

end = time.process_time()

print("Time elapsed: ", end - start)  # seconds
print("Time elapsed: ", timedelta(seconds=end-start))

start = time.process_time()

arr1 = [i for i in range(10000000)]
arr2 = [i for i in range(10000000, 0, -1)]
sum = 0

for num1, num2 in zip(arr1, arr2):
    sum += num1 + num2

end = time.process_time()

print("Time elapsed: ", end - start)  # seconds
print("Time elapsed: ", timedelta(seconds=end-start))