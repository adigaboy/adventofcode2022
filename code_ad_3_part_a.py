def remove_dup(s):
    r = list(s)
    for curr in range(len(s) - 1):
        for seeker in range(curr + 1, len(s)):
            if s[curr] == s[seeker]:
                r[seeker] = '#'
    return list(filter(lambda a: a != '#', r))

def only_dup(left, right):
    res = []
    for c_left in left:
        for c_right in right:
            if c_left == c_right:
                res.append(c_left)
    return res

with open("C:/Users/sysadm/Downloads/input.txt", 'r') as f:
    result = 0
    for line in f:
        line = line.rstrip()
        curr_shared = []

        line_len = len(line)

        first = remove_dup(line[:int(line_len/2)])
        second = remove_dup(line[int(line_len/2):])

        dups = only_dup(first, second)
        for d in dups:
            if d[0].isupper():
                result += ord(d) - ord('A') + 27
            else:
                result += ord(d) - ord('a') + 1
    print(result)
