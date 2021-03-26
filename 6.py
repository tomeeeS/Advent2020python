# https://adventofcode.com/2020/day/6

def compute(x):
    lines = x.split('\n')
    intersection = set(lines[0])
    for i in range(1, len(lines)):
        intersection = intersection.intersection(lines[i])
    return intersection


with open('6.txt') as f:
    # noinspection PyTypeChecker
    entries = [
        compute(x)
        for x in
        ''.join(f.readlines()).split('\n\n')
    ]

if __name__ == '__main__':
    print(
        sum([len(x) for x in entries])
    )
