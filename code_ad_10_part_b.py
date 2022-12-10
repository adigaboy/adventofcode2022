
import sys

cycles = {
    'noop': 1,
    'addx': 2
}

def draw_pos_in_sprite(draw_pos, sprite_pos):
    return True if draw_pos in sprite_pos else False

if __name__ == "__main__":
    file = sys.argv[1]

    def read_from_file(file_name):
        inputs = []

        with open(file_name) as f:
            for line in f:
                input = line.rstrip().split(' ')
                inputs.append(input)

        curr_cycle = 0
        drawing = [['.' for _ in range(40)] for _ in range(6)]
        sprite_position = [0, 1, 2]
        draw_position = 0
        line_position = 0
        for input in inputs:
            # draw pixels while executing
            for i in range(cycles[input[0]]):
                if draw_pos_in_sprite(draw_position, sprite_position):
                    drawing[line_position][draw_position] = '#'
                draw_position += 1
                curr_cycle += 1
                if curr_cycle % 40 == 0:
                    draw_position = 0
                    line_position += 1
            # move sprit to new location
            if input[0] == 'addx':
                sprite_position = [x + int(input[1]) for x in sprite_position]
        for i in drawing:
            print(i)
    read_from_file(file)
