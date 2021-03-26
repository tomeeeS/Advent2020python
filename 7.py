# https://adventofcode.com/2020/day/6

import re


def finish(bag_name, i):
    entries[bag_name] = (i, entries[bag_name][1])
    return i


def compute(x):
    entry = entries[x]
    if entry[0] is not None:
        return entry[0]

    if entry[1][0][1] == 'other':
        return finish(x, 1)
    sum_ = sum([
        int(i[0]) * compute(i[1])
        for i in entry[1]
    ]) + 1
    return finish(x, sum_)


def parse(x):
    definition = x.split(' bags contain')
    contained_bags = re.sub(
            '.\n| bags?'
            , '',
            definition[1]
        )
    contained_bags = contained_bags.strip() \
        .split(', ')
    values_split = [
        x.split(' ', 1)
        for x in contained_bags
    ]
    values = [
        (x[0], x[1])
        for x in values_split
    ]
    return tuple([
        ''.join(definition[0]),
        (None, values)
    ])


with open('7.txt') as f:
    # noinspection PyTypeChecker
    entries = dict([
        parse(x)
        for x in
        f.readlines()
    ])

if __name__ == '__main__':
    print(compute('shiny gold') - 1)
