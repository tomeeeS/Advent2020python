# https://adventofcode.com/2020/day/4

import re


def is_length_valid(x):
    return len(x) == 8 \
        or len(x) == 7 \
        and 'cid' not in x.keys()


def is_height_valid(x):
    height = re.split('[ic]', x['hgt'])
    if len(height) < 2:
        return False
    if height[1] == 'm':
        result = 150 <= int(height[0]) <= 193
    else:
        result = 59 <= int(height[0]) <= 76
    return result


def is_hair_color_valid(x):
    return bool(re.fullmatch(
        '#[0-9a-f]{6}',
        x['hcl']
    ))


def is_eye_color_valid(x):
    return x['ecl'] in [
        'amb',
        'blu',
        'brn',
        'gry',
        'grn',
        'hzl',
        'oth'
    ]


def is_passport_valid(x):
    return bool(re.fullmatch(
        '[0-9]{9}',
        x['pid']
    ))


# noinspection PyChainedComparisons
def are_values_valid(x):
    return 1920 <= int(x['byr']) <= 2002 \
        and 2010 <= int(x['iyr']) <= 2020 \
        and 2020 <= int(x['eyr']) <= 2030 \
        and is_height_valid(x) \
        and is_hair_color_valid(x) \
        and is_eye_color_valid(x) \
        and is_passport_valid(x)


def is_valid(x):
    return is_length_valid(x) \
        and are_values_valid(x)


with open('4.txt') as f:
    # noinspection PyTypeChecker
    entries = [
        dict([
            tuple(y.split(':'))
            for y in
            [i for i in re.split('[ \n]', x) if i]  # [i for i in _ if i]: removes empty strings
        ])
        for x in
        ''.join(f.readlines()).split('\n\n')
    ]

if __name__ == '__main__':
    print(
        len([
            x for x in
            entries
            if is_valid(x)
        ])
    )
