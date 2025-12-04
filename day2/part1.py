import time
start: float = time.perf_counter()

invalid_ids: int = 0
ranges: list = open("input.txt", "r").read().split(",") # split into a list of strings like ['12-44', '2235-30432', etc.]

for r in ranges:
    rn: list[str] = r.split("-") # ex. split '42-323' into ['42', '323']

    for num in range(int(rn[0]), int(rn[1]) + 1): # every number from 42 to 323, including 323
        num_id: str = str(num)
        l = len(num_id)
        if l % 2 == 1:
            continue # filter out numbers with odd lengths since they can't have repeating patterns

        ind: int = int(l/2) # half of total length

        if num_id[ind:] == num_id[:ind]: # if first half of string is the same as second half of string
            invalid_ids += num

print(invalid_ids)
end: float = time.perf_counter()
print(f"{(end - start)*100} ms")