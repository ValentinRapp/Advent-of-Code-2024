with open("input.txt", "r") as file:
    grid = file.read().splitlines()

# part 1

pattern = 'XMAS'

directions = [
    (0, 1),
    (1, 0),
    (1, 1),
    (-1, 1),
    (1, -1),
    (-1, -1),
    (0, -1),
    (-1, 0)
]

rows = len(grid)
cols = len(grid[0]) if rows > 0 else 0
s = 0

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == pattern[0]:
            for direction in directions:
                di, dj = direction
                found = True
                for k in range(1, len(pattern)):
                    ni, nj = i + k * di, j + k * dj
                    if not (0 <= ni < rows and 0 <= nj < cols) or grid[ni][nj] != pattern[k]:
                        found = False
                        break
                if found:
                    s += 1

print(f"part 1: {s}")

# part 2

s = 0

for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[0]) - 1):
        if grid[i][j] == 'A':
            step = 0
            if ((grid[i-1][j-1] == 'M') and (grid[i+1][j+1] == 'S')) or ((grid[i-1][j-1] == 'S') and (grid[i+1][j+1] == 'M')):
                step += 1
            if ((grid[i-1][j+1] == 'M') and (grid[i+1][j-1] == 'S')) or ((grid[i-1][j+1] == 'S') and (grid[i+1][j-1] == 'M')):
                step += 1
            
            if step == 2:
                s += 1

print(f"part 2: {s}")
