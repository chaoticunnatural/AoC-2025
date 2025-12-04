rolls_rows: list[list[str]] = [list(row) for row in open("input.txt", "r").read().splitlines()]

accessible: int = 0

height: int = len(rolls_rows)
width: int = len(rolls_rows[0])

adj_positions: list[tuple[int, int]] = [ # 8 adjacent positions rolls might be in relative to any roll which would be at (0, 0)
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1), # yes i did format it like this it looks nice okay
    ( 1, -1), ( 1, 0), ( 1, 1)
]

for row in range(height):
    for column in range(width):
        if rolls_rows[row][column] == ".":
            continue

        adjacent: int = sum( # add one to adjacent rolls if the string at a given position is "@"
            1 for adj_r, adj_c in adj_positions
            if 0 <= row + adj_r < height and 0 <= column + adj_c < width
            and rolls_rows[row + adj_r][column + adj_c] == "@"
        )

        if adjacent < 4:
            accessible += 1

print(accessible)