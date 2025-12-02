with open('input.txt', 'r') as rotations_f:
    rotations: list[str] = rotations_f.read().splitlines() # split into list like ['L29', 'R45', etc.]

    password: int = 0
    current_loc: int = 50 # starts at 50 (i definitely didn't think my code was wrong for 10 minutes because i missed this)

    for rotation in rotations:
        dir_mult: int = -1 if rotation[0] == "L" else 1 # negative if going left
        steps: int = int(rotation[1:])

        current_loc += steps * dir_mult # make steps negative if left (dir_mult = -1)

        if current_loc % 100 == 0: # check if the remainder if dividing location by 100 is zero, instead of having the number wrap around
            password += 1

    print(password)