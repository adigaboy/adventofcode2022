import sys
from typing import Dict, List

if __name__ == "__main__":
    file = sys.argv[1]

    positions = set([(0, 0)])
    rope_parts = [[0, 0] for _ in range(10)]

    def read_from_file(file_name):
        with open(file_name) as f:
            for line in f:
                line = line.rstrip()
                direction = line[0]
                steps = int(line[2:])
                for _ in range(steps):
                    if direction == 'U':
                        rope_parts[0][0] += 1
                    elif direction == 'D':
                        rope_parts[0][0] -= 1
                    elif direction == 'R':
                        rope_parts[0][1] += 1
                    else:
                        rope_parts[0][1] -= 1
                    for j in range(9):
                        dx = rope_parts[j][1] - rope_parts[j + 1][1]
                        dy = rope_parts[j][0] - rope_parts[j + 1][0]

                        if dx == 2:
                            if dy > 0:
                                rope_parts[j + 1][0] += 1
                            elif dy < 0:
                                rope_parts[j + 1][0] -= 1
                            rope_parts[j + 1][1] += 1
                        elif dx == -2:
                            if dy > 0:
                                rope_parts[j + 1][0] += 1
                            elif dy < 0:
                                rope_parts[j + 1][0] -= 1
                            rope_parts[j + 1][1] -= 1
                        elif dy == 2:
                            if dx > 0:
                                rope_parts[j + 1][1] += 1
                            elif dx < 0:
                                rope_parts[j + 1][1] -= 1
                            rope_parts[j + 1][0] += 1
                        elif dy == -2:
                            if dx > 0:
                                rope_parts[j + 1][1] += 1
                            elif dx < 0:
                                rope_parts[j + 1][1] -= 1
                            rope_parts[j + 1][0] -= 1
                            # xxxxxx    xxxxHx  xxxxHx  xxxxHx
                            # xxxxHx    xxxxxx  xxxxHx  xxxxHx
                            # xxxHxx    xxxHxx  xxxxxx  xxxTxx
                            # xxTxxx    xxTxxx  xxTxxx  xxxxxx
                    positions.add((rope_parts[9][0], rope_parts[9][1]))
        total_spots = 0
        total_spots = len(positions)
        print(total_spots)
    read_from_file(file)
