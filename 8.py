# https://adventofcode.com/2020/day/6

import re


def parse(x):
    a = x.split()
    return a[0], int(a[1])


with open('8.txt') as f:
    # noinspection PyTypeChecker
    entries = [
        parse(x)
        for x in
        f.readlines()
    ]

if __name__ == '__main__':
    print(entries)
