from functools import cmp_to_key
import sys


def parse_line(line: str):
    parsed_list = [[]]
    curr_list = parsed_list[-1]
    prev_list = curr_list
    to_append = ''
    for c in line:
        if c == '[':
            curr_list.append([])
            prev_list = curr_list
            curr_list = curr_list[-1]
        elif c in [']', ',']:
            if to_append != '':
                curr_list.append(int(to_append))
                to_append = ''
            if c == ']':
                curr_list = prev_list
        else:
            to_append += c
    return parsed_list[0][0]

def rec_check_pairs(left_side, right_side):
    if isinstance(right_side, int) and isinstance(left_side, int):
        if  left_side > right_side:
            return -1
        if left_side < right_side:
            return 1
        return 0
    if isinstance(left_side, list) or isinstance(right_side, list):
        if isinstance(right_side, int):
            right_side = [right_side]
        if isinstance(left_side, int):
            left_side = [left_side]
    if len(left_side) == 0 and len(right_side) > 0:
        return 1
    for i in range(len(left_side)):
        if i >= len(right_side):
            return -1
        ret = rec_check_pairs(left_side[i], right_side[i])
        if ret:
            return ret
    if len(left_side) < len(right_side):
        return 1


if __name__  == '__main__':
    filename = sys.argv[1]
    pairs = []
    with open(filename) as f:
        for line in f:
            if line.rstrip() != '':
                pairs.append(eval(line.rstrip()))

    right_ordered_pairs = []
    for i, (left_side, right_side) in enumerate(zip(pairs[::2], pairs[1::2])):
        if rec_check_pairs(left_side, right_side) >= 1:
            right_ordered_pairs.append(i + 1)

    print(sum(right_ordered_pairs))

    markers = [[[2]], [[6]]]
    s = sorted(pairs + markers, key=cmp_to_key(rec_check_pairs), reverse=True)
    idx1, idx2 = [s.index(p) for p in s if p in markers]
    print((idx1 + 1) * (idx2 + 1))