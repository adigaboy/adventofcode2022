import numpy as np
from copy import deepcopy
import sys
from typing import List


def solve_part_a(input_trees):
    def look_left(array: List[int]):
        visible_trees_in_line = []
        curr_max = -1
        for num in array:
            if num <= curr_max:
                visible_trees_in_line.append(0)
                continue
            else:
                visible_trees_in_line.append(1)
                curr_max = num
        return visible_trees_in_line

    def look_right(array: List[int]):
        visible_trees_in_line = list(reversed(look_left(array)))
        return visible_trees_in_line

    visible_trees = []
    for i, trees_array in enumerate(input_trees):
        visible_trees.append(look_left(trees_array))
        for j, is_visible in enumerate(look_right(reversed(trees_array))):
            visible_trees[i][j] += is_visible
    
    trans_input_trees = np.array(input_trees).transpose()

    trans_visible_trees = []
    for i, trees_array in enumerate(trans_input_trees):
        trans_visible_trees.append(look_left(trees_array))
        for j, is_visible in enumerate(look_right(reversed(trees_array))):
            trans_visible_trees[i][j] += is_visible

    for i, line_of_trees in enumerate(np.array(trans_visible_trees).transpose()):
        for j, tree in enumerate(line_of_trees):
            visible_trees[i][j] += tree
    
    visible_trees_tot = 0
    for i, line_of_trees in enumerate(visible_trees):
        for j, tree in enumerate(line_of_trees):
            if tree != 0:
                visible_trees[i][j] = 1
                visible_trees_tot += 1
    return visible_trees_tot

def solve_part_b(input_trees):
    def look_left(array: List[int]):
        visible_trees_in_line = []
        for i, num in enumerate(array):
            trees_seen = 1
            for curr in reversed(array[:i]):
                if curr < num:
                    trees_seen += 1
                else:
                    visible_trees_in_line.append(trees_seen)
                    break
            else:
                visible_trees_in_line.append(trees_seen - 1)
        return visible_trees_in_line

    def look_right(array: List[int]):
        visible_trees_in_line = list(reversed(look_left(array)))
        return visible_trees_in_line

    def multiply_array(array):
        result = 1
        for number in array:
            result *= number
        return result

    left_visible_trees = []
    right_visible_trees = []
    for trees_array in input_trees:
        left_visible_trees.append(look_left(trees_array))
        right_visible_trees.append(look_right(list(reversed(trees_array))))

    trans_input_trees = np.array(input_trees).transpose()
    up_visible_trees = []
    down_visible_trees = []

    for trees_array in trans_input_trees:
        up_visible_trees.append(look_left(trees_array))
        down_visible_trees.append(look_right(list(reversed(trees_array))))

    up_visible_trees = np.array(up_visible_trees).transpose()
    down_visible_trees = np.array(down_visible_trees).transpose()
    max_scenic_scores = 0
    for i in range(len(left_visible_trees)):
        max_scenic_scores = max(max_scenic_scores, max([multiply_array(x) for x in zip(left_visible_trees[i], right_visible_trees[i], up_visible_trees[i], down_visible_trees[i])]))

    return max_scenic_scores

if __name__ == "__main__":
    part = sys.argv[1]
    file = sys.argv[2]

    input_trees = []

    def read_from_file(file_name):
        with open(file_name) as f:
            for line in f:
                line = line.rstrip()
                input_trees.append([int(x) for x in line])

    read_from_file(file)

    if part == 'a':
        print(solve_part_a(input_trees))
    elif part == 'b':
        print(solve_part_b(input_trees))
