# https://adventofcode.com/2020/day/17
# Conway cubes


with open('17.txt') as f:
    # noinspection PyTypeChecker
    inputs = [
        x
        for x in
        f.readlines()
    ]


cycles = 6
input_size = len(inputs)
xy_dim = input_size + (cycles + 1) * 2  # '+ 1': we need to index one farther for the calculations
z_dim = 1 + (cycles + 1) * 2

# size: z_dim * xy_dim * xy_dim
cubes = [False]


def parse(c):
    return c == '#'


if __name__ == '__main__':
    for i in range(input_size):
        for j in range(input_size):
            cubes[0][i][j] = parse(inputs[i][j])
    print(cubes[0][7][7])
