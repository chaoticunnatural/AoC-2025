rolls_rows: list[list[str]] = [list(row) for row in open("input.txt", "r").read().splitlines()]

accessible: int = 0
height: int = len(rolls_rows)
width: int = len(rolls_rows[0])

adj_positions: list[tuple[int, int]] = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]

while True:
    to_remove: list[tuple[int, int]] = []

    for row in range(height):
        for column in range(width):
            if rolls_rows[row][column] != "@":
                continue

            adjacent: int = sum(
                1
                for adj_r, adj_c in adj_positions
                if 0 <= row + adj_r < height
                and 0 <= column + adj_c < width
                and rolls_rows[row + adj_r][column + adj_c] == "@"
            )

            if adjacent < 4:
                accessible += 1
                to_remove.append((row, column))

    if not to_remove:
        break

    for r, c in to_remove:
        rolls_rows[r][c] = "."

print(accessible)