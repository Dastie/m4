line = input()

def check(line):
    if line == line[::-1]:
        return True
    else:
        return False

print(check(line))

# print(check(line))