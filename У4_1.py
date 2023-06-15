"""  """

line = 'sdfsdfsd'
def counter(line):
    for n in set(line):
        res = [i for i in line if i == n]
        print(f'{n} - {len(res)}')

counter(line)

print('-'*100)

def strcounter(line):
    for sym in set(line):
        count = 0
        for sub_sym in line:
            if sym == sub_sym:
                count += 1
        print(f'{sym} - {count}')

strcounter(line)
print('-'*100)

def counte(line):
    sym_dict = {}
    for sym in line:
        sym_dict[sym] = 1 + sym_dict.get(sym, 0)

    for sym, count in sym_dict.items():
        print(f'{sym} - {count}')

counte(line)
print('-'*100)

def c(line):
    for sym in set(line):
        print(f'{sym} - {line.count(sym)}')

c(line)