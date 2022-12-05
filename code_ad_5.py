stacks = [
    ['H', 'T', 'Z', 'D'],
    ['Q', 'R', 'W', 'T', 'G', 'C', 'S'],
    ['P', 'B', 'F', 'Q', 'N', 'R', 'C', 'H'],
    ['L', 'C', 'N', 'F', 'H', 'Z'],
    ['G', 'L', 'F', 'Q', 'S'],
    ['V', 'P', 'W', 'Z', 'B', 'R', 'C', 'S'],
    ['Z', 'F', 'J'],
    ['D', 'L', 'V', 'Z', 'R', 'H', 'Q'],
    ['B', 'H', 'G', 'N', 'F', 'Z', 'L', 'D']
]

# PART A
# with open("C:/Users/sysadm/Downloads/input5.txt", 'r') as f:
#     for line in f:
#         to_move = int(line[5:7].rsplit()[0])
#         if to_move > 9:
#             fix = 1
#         else:
#             fix = 0
#         from_stack = int(line[12+fix]) - 1
#         to_stack = int(line[17+fix]) - 1
#         crates_to_move = stacks[from_stack][-to_move:]
#         crates_to_move.reverse()
#         stacks[from_stack] = stacks[from_stack][:-to_move]
#         stacks[to_stack] += crates_to_move
    
#     for stack in stacks:
#         print(stack[-1])

# PART B
with open("C:/Users/sysadm/Downloads/input5.txt", 'r') as f:
    for line in f:
        to_move = int(line[5:7].rsplit()[0])
        if to_move > 9:
            fix = 1
        else:
            fix = 0
        from_stack = int(line[12+fix]) - 1
        to_stack = int(line[17+fix]) - 1
        stacks[to_stack] += stacks[from_stack][-to_move:]
        stacks[from_stack] = stacks[from_stack][:-to_move]
    
    for stack in stacks:
        print(stack[-1])
