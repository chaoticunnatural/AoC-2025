import time
start: float = time.perf_counter()

ranges: list[range] = []
numbers: list[int] = []

fresh: int = 0

for line in open("input.txt", "r"): # create list of ranges and list of numbers
    line = line.strip()
    if not line:
        continue

    if "-" in line:
        rn = line.split("-")
        ranges.append(range(int(rn[0]), int(rn[1])+1))
    else:
        numbers.append(int(line))

for n in numbers:
    for rng in ranges:
        if n in rng:
            fresh += 1
            break

print(fresh)
end: float = time.perf_counter()
print(f"{(end - start)*100} ms")