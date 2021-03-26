# https://adventofcode.com/2020/day/1

with open('1.txt') as f:
    array = [int(line) for line in f]


if __name__ == '__main__':
    for i, expense1 in enumerate(array):
        for j, expense2 in enumerate(array[0:i]):
            for expense3 in array[0:j]:
                if expense1 + expense2 + expense3 == 2020:
                    mult = expense1 * expense2 * expense3
    print(
        mult
    )
