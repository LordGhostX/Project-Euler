"""Problem 15: Lattice paths

Starting in the top left corner of a 2 2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20 20 grid?"""

grid_size = 21

grid = []
for _ in range(grid_size):
    grid.append([0] * grid_size)

start, end = [0] * 2, [grid_size - 1] * 2

possible_paths = [[start]]
successful_paths = 0

while len(possible_paths) != 0:
    for i in possible_paths:
        i_0, i_1 = i[-1][0], i[-1][1]
        if [i_0, i_1] != end:
            if (grid_size - 1) > i_0:
                new_path = i + [[i_0 + 1, i_1]]
                possible_paths.append(new_path)
            if (grid_size - 1) > i_1:
                new_path = i + [[i_0, i_1 + 1]]
                possible_paths.append(new_path)
        else:
            successful_paths += 1
        possible_paths.remove(i)

print(successful_paths)
