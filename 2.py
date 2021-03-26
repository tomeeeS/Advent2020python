# https://adventofcode.com/2020/day/2

class Data:
    def __init__(self, data):
        positions = data[0].split('-')

        self.pos1 = int(positions[0]) - 1
        self.pos2 = int(positions[1]) - 1
        self.required_char = data[1][0]
        self.pw = data[2]


def validate(data):
    does_first_position_match = (data.pw[data.pos1] == data.required_char)
    does_second_position_match = (data.pw[data.pos2] == data.required_char)
    return does_first_position_match != does_second_position_match


with open('2.txt') as f:
    inputs = [Data(x.split(' ')) for x in f.readlines()]

if __name__ == '__main__':
    print(
        len(
            list(filter(
                validate,
                inputs
            ))
        )
    )
