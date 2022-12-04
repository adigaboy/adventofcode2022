
def is_a_in_b(a: str, b: str):
    a_r = a.split('-')
    b_r = b.split('-')

    if int(a_r[0]) >= int(b_r[0]) and int(a_r[1]) <= int(b_r[1]):
        return True
    return False

with open("C:/Users/sysadm/Downloads/input4.txt", 'r') as f:
    result = 0
    for line in f:
        splited = line.split(',')
        if is_a_in_b(splited[0], splited[1]) or is_a_in_b(splited[1], splited[0]):
            result += 1
    print(result)
