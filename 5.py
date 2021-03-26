# https://adventofcode.com/2020/day/5

with open('5.txt') as f:
    inputs = [
        '0b' + x.replace('B', '1')
            .replace('F', '0')
            .replace('R', '1')
            .replace('L', '0')
        for x in
        f.readlines()
    ]

if __name__ == '__main__':
    stored_seat_ids = [int(x, 2) for x in inputs]
    all_seat_ids = list(range(min(stored_seat_ids), max(stored_seat_ids) + 1))
    for x in stored_seat_ids:
        all_seat_ids.remove(x)
    print(
        all_seat_ids[0]
    )
