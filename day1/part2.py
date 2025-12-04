import time
start: float = time.perf_counter()

rotations: list[str] = open('input.txt', 'r').read().splitlines() # split into list like ['L29', 'R45', etc.]

password: int = 0
current_loc: int = 50 # starts at 50 (i definitely didn't think my code was wrong for 10 minutes because i missed this)

for rotation in rotations:
    dir_inc: int = -1 if rotation[0] == "L" else 1 # make direction negative if left because going it's going backwards
    steps: int = int(rotation[1:]) # all chars in the string after 0 (the letter)

    for s in range(0, steps):
        current_loc += dir_inc # step once

        if current_loc % 100 == 0:
            password += 1

print(password)
end: float = time.perf_counter()
print(f"{(end - start)*100} ms")