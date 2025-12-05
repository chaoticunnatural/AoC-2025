import time
start: float = time.perf_counter()

end: float = time.perf_counter()
print(f"{(end - start)*100} ms")