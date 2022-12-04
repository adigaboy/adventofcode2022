def is_a_in_b(a, b):
    if a[0] >= b[0] and a[1] <= b[1]:
        return True
    return False

def is_a_and_b_overlap(a, b):
    if a[0] >= b[0] and a[0] <= b[1]:
        return True
    if b[0] >= a[0] and b[0] <= a[1]:
        return True
    return False

with open("C:/Users/sysadm/Downloads/input4.txt", 'r') as f:
    result = 0
    for line in f:
        splited = line.split(',')
        a_r = [int(x) for x in splited[0].split('-')]
        b_r = [int(x) for x in splited[1].split('-')]
        if is_a_in_b(a_r, b_r) or is_a_in_b(b_r, a_r):
            result += 1
        else:
            if is_a_and_b_overlap(a_r, b_r):
                result += 1
    print(result)
