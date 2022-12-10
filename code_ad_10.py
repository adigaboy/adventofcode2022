
import sys

cycles = {
    'noop': 1,
    'addx': 2
}


def if_record_signal(input: str, curr_cycle: int, target_base: int):
    if curr_cycle % target_base == 0 or input == 'addx' and curr_cycle % target_base == target_base - 1:
        return True
    return False

def round_cycle(curr, traget_base):
    return curr if curr % traget_base == 0 else curr + 1


if __name__ == "__main__":
    file = sys.argv[1]

    def read_from_file(file_name):
        signal_strength = 0
        x = 1
        curr_cycle = 1
        inputs = []
        
        with open(file_name) as f:
            for line in f:
                input = line.rstrip().split(' ')
                inputs.append(input)
        
        for input in inputs:
            if if_record_signal(input[0], curr_cycle - 20, 40):
                signal_strength += (round_cycle(curr_cycle - 20, 40) + 20) * x
            curr_cycle += cycles[input[0]]
            x += 0 if input[0] == 'noop' else int(input[1])
        print(signal_strength)
    read_from_file(file)
