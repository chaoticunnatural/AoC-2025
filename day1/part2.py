with open('input.txt', 'r') as f:
    rotations: list[str] = f.read().splitlines()

    password: int = 0
    current_loc: int = 50

    for rotation in rotations:
        dir_inc: int = -1 if rotation[0] == "L" else 1
        steps: int = int(rotation[1:])

        for s in range(0, steps):
            current_loc += dir_inc

            if current_loc % 100 == 0:
                password += 1

    print("password: " + str(password))