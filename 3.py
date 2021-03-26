# https://adventofcode.com/2020/day/3

with open('3.txt') as f:
    inputs = f.readlines()

if __name__ == '__main__':
    arboreal_cost = 1  # (answer)
    biome_pattern_width = len(inputs[0]) - 1  # input width.  (- 1): \n at the end
    toboggan_control_configurations = [
        [1, 1],
        [1, 3],
        [1, 5],
        [1, 7],
        [2, 1]
    ]

    for z in toboggan_control_configurations:
        y = 0
        tree_count = 0
        for x in range(0, len(inputs), z[0]):
            if inputs[x][y] == '#':
                tree_count += 1
            y = (y + z[1]) % biome_pattern_width
        arboreal_cost *= tree_count

    print(
        arboreal_cost
    )
