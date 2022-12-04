def remove_dup(s):
    r = list(s)
    for curr in range(len(s) - 1):
        for seeker in range(curr + 1, len(s)):
            if s[curr] == s[seeker]:
                r[seeker] = '#'
    return list(filter(lambda a: a != '#', r))

def only_dup(group):
    for c in group[0]:
        for d in group[1]:
            for e in group[2]:
                if c == d and d == e:
                    return c

with open("C:/Users/sysadm/Downloads/input.txt", 'r') as f:
    dups = []
    result = 0
    groups = [[]]
    i = 0
    for line in f:
        to_append = list(remove_dup(line.rstrip()))
        to_append.sort()
        if i < 3:
            groups[-1].append(to_append)
            i += 1
        else:
            groups.append([to_append])
            i = 1
    for group in groups:
        dups.append(only_dup(group))
    for d in dups:
        if d[0].isupper():
            result += ord(d) - ord('A') + 27
        else:
            result += ord(d) - ord('a') + 1
    print(result)
