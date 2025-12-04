import time
start: float = time.perf_counter()
invalid_ids: int = 0
ranges: list = open("input.txt", "r").read().split(",")  # split into a list of strings like ['12-44', '2235-30432', etc.]

for r in ranges:
    rn: list[str] = r.split("-")  # ex. split '42-323' into ['42', '323']

    for num in range(int(rn[0]), int(rn[1]) + 1): # every number from 42 to 323, including 323
        num_id = str(num)
        if num_id in (num_id+num_id)[1:-1]:
            # check if num_id exists in a duplicat of itself, removing the first and last characters to avoid a full match
            # ex. num_id = 123123123, (num_id+num_id)[1:-1] = 2312312312312312, and num_id exists in that string
            invalid_ids += num

print(invalid_ids)
end: float = time.perf_counter()
print(f"{(end - start)*100} ms")