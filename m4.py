line = input()

def check(line):
    if list(line) == list(reversed(line)):
        return True
    else:
        return False

print(check(line))