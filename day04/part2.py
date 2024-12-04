with open("input.txt", "r") as file:
    grid = file.read().splitlines()

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


print(s)