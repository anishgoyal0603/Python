import time

large_list = list(range(1_000_000))
large_set = set(range(1_000_000))
target = 999999

start = time.time()
result = target in large_list
list_time = time.time() - start

start = time.time()
result = target in large_set
set_time = time.time() - start

print(f"List lookup time:  {list_time:.6f} seconds")
print(f"Set lookup time:   {set_time:.6f} seconds")