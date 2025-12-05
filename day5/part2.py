import time
start: float = time.perf_counter()

ranges: list[tuple[int, int]] = []
merged: list[list[int]] = []

for line in open("input.txt", "r"): # create list of ranges and list of numbers
    line = line.strip()
    if not line: # stop at the blank dividing line
        break

    if "-" in line:
        rna, rnb = map(int, line.split("-"))
        ranges.append((rna, rnb))

ranges.sort()  # sort by start because yes

for range_s, range_e in ranges:
    if not merged or range_s > merged[-1][1] + 1: # next range begins after last one with at least one number in between

        merged.append([range_s, range_e]) # add a new range if no overlap
    else:
        merged[-1][1] = max(merged[-1][1], range_e) # merge with existing range by extending the end value

print(sum((b - a) + 1 for a, b in merged)) # number of values in a range is (b - a) + 1 so just sum of all
end: float = time.perf_counter()
print(f"{(end - start)*100} ms")