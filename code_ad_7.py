import sys
from typing import Dict


def solve_part_a(main_dirs):
    sol = [0]

    def rec_calc_sol(curr_dir: Dict[str, Dict], sol):
        '''
        calculate sizes for dirs that are smaller than 100000
        '''
        if not curr_dir:
            return

        for dir in curr_dir.keys():
            if dir == 'size':
                if curr_dir['size'] <= 100000:
                    sol[0] += curr_dir['size']
            else:
                rec_calc_sol(curr_dir[dir], sol)
    rec_calc_sol(main_dirs['/'], sol)
    return sol[0]

def solve_part_b(main_dirs):
    space_taken = main_dirs['/']['size']
    space_to_free = 30000000 - (70000000 - space_taken)
    min_size_to_free = [70000000]

    def rec_find_dir(curr_dir: Dict[str, Dict], min_size_to_free):
        '''
        find the dir that is smallest to delete to free enough space
        '''
        if not curr_dir:
            return
        for dir in curr_dir.keys():
            if dir == 'size':
                if curr_dir['size'] >= space_to_free:
                    if curr_dir['size'] < min_size_to_free[0]:
                        min_size_to_free[0] = curr_dir['size']
            else:
                rec_find_dir(curr_dir[dir], min_size_to_free)

    rec_find_dir(main_dirs['/'], min_size_to_free)
    return min_size_to_free[0]

if __name__ == "__main__":
    part = sys.argv[1]
    file = sys.argv[2]
    
    dirs = {}

    def return_to_parent_dir(path):
        '''
        return to the parent dir
        '''
        curr_dir = dirs
        for dir in path:
            curr_dir = curr_dir[dir]
        return curr_dir

    def read_from_file(file_name):
        with open(file_name) as f:
            dir_path = []
            curr_dir = dirs
            for line in f:
                line = line.rstrip()
                if line.startswith('$'):
                    if line == '$ cd ..':
                        # go back to parent dir
                        dir_path.pop()
                        curr_dir = return_to_parent_dir(dir_path)
                    elif line.startswith('$ cd '):
                        # add new dir to dirs dict
                        dir_name = line[5:]
                        dir_path.append(dir_name)
                        curr_dir[dir_name] = {'size': 0}
                        curr_dir = curr_dir[dir_name]
                else:
                    if not line.startswith('dir'):
                        curr_dir['size'] += int(line.split(' ')[0])

        def rec_calc_tot_sizes(curr_dir: Dict[str, Dict]):
            '''
            calculate total sizes of dirs recursively
            '''
            if not curr_dir:
                return 0

            for dir in curr_dir.keys():
                if dir != 'size':
                    curr_dir['size'] += rec_calc_tot_sizes(curr_dir[dir])

            return curr_dir['size']

        rec_calc_tot_sizes(dirs['/'])

    read_from_file(file)
    if part == 'a':
        print(solve_part_a(dirs))
    elif part == 'b':
        print(solve_part_b(dirs))
