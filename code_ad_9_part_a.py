import sys
from typing import Dict, List


def is_diagonal(pos_diff: int):
    if pos_diff in [1,3, 7, 9]:
        return True
    return False

def check_new_raw_positions(record: Dict[int, Dict[int, int]], next_raw: int):
    if not record.get(next_raw):
        record[next_raw] = {}

def move_diag(tail_position: List[int], diffs: Dict[str, int], record: Dict[int, Dict[int, int]]):
    if abs(diffs['horizontal']) == 1 and abs(diffs['vertical']) > 1:
        if diffs['vertical'] > 0:
            vertical_move = 1
        else:
            vertical_move = -1
        tail_position[0] += vertical_move
        tail_position[1] += diffs['horizontal']
        diffs['vertical'] -= vertical_move
        diffs['horizontal'] = 0
    elif abs(diffs['horizontal']) > 1 and abs(diffs['vertical']) == 1:
        if diffs['horizontal'] > 0:
            horizontal_move = 1
        else:
            horizontal_move = -1
        tail_position[0] += diffs['vertical']
        tail_position[1] += horizontal_move
        diffs['vertical'] = 0
        diffs['horizontal'] -= horizontal_move
    check_new_raw_positions(record, tail_position[0])
    record[tail_position[0]][tail_position[1]] = 1

def move_tail(tail_position: List[int], head_position: List[int], record: Dict[int, Dict[int, int]]):
    diffs = {
        'horizontal': head_position[1] - tail_position[1],
        'vertical': head_position[0] - tail_position[0]
    }
    move_diag(tail_position, diffs, record)

    if diffs['vertical'] > 1:
        for i in range(1, diffs['vertical']):
            check_new_raw_positions(record, tail_position[0] + i)
            record[tail_position[0] + i][tail_position[1]] = 1
        tail_position[0] += diffs['vertical'] - 1
    elif diffs['vertical'] < -1:
        for i in range(diffs['vertical'] + 1, 0):
            check_new_raw_positions(record, tail_position[0] + i)
            record[tail_position[0] + i][tail_position[1]] = 1
        tail_position[0] += diffs['vertical'] + 1
    elif diffs['horizontal'] > 1:
        for i in range(1, diffs['horizontal']):
            record[tail_position[0]][tail_position[1] + i] = 1
        tail_position[1] += diffs['horizontal'] - 1
    elif diffs['horizontal'] < -1:
        for i in range(diffs['horizontal'] + 1, 0):
            record[tail_position[0]][tail_position[1] + i] = 1
        tail_position[1] += diffs['horizontal'] + 1

# xxHxx   xHxxx   xxTxx   xTxxx
# xxxxx   xxxxx   xxTxx   xxTxx
# xxTxx   xTxxx   xxxxx   xxxxx
# xTxxx   xxTxx   xHxxx   xxHxx

# xTxxx   xxxxHx
# xxxxH   xTxxxx

def update_head_pos(head_position: List[int], direction: str, steps: int):
    if direction == 'U':
        head_position[0] += steps
    elif direction == 'D':
        head_position[0] -= steps
    elif direction == 'R':
        head_position[1] += steps
    else:
        head_position[1] -= steps


if __name__ == "__main__":
    # part = sys.argv[1]
    file = 'input9.txt'

    positions = {0: {}}

    def read_from_file(file_name):
        tail_pos = [0, 0]
        head_pos = [0, 0]
        with open(file_name) as f:
            for line in f:
                line = line.rstrip()
                direction = line[0]
                steps = int(line[2:])
                update_head_pos(head_pos, direction, steps)
                move_tail(tail_pos, head_pos, positions)

        total_spots = 0
        for k in positions:
            total_spots += len(positions[k])
        print(total_spots)
    read_from_file(file)
