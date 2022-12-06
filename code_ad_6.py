def check_for_dup(s: str):
    for i, c in enumerate(s):
        for k in s[i+1:]:
            if c == k:
                return False
    return True

unique_chars = 4

with open("C:/Users/sysadm/Downloads/input6.txt", 'r') as f:
    line = f.readline()
    i = 0
    while i < len(line) - unique_chars:
        window = line[i:i+unique_chars]
        if check_for_dup(window):
            print(i+unique_chars)
            break
        i += 1
