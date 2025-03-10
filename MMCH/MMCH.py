f = open("rosalind_mmch.txt", 'r')
raw_data = f.read()
data = raw_data.split('>Rosalind_')
data = data[1:]
RNA_seq = data[0][4:].replace('\n', '')


def permutation(n, m):
    value = 1
    for i in range(n, n-m, -1):
        value = i*value
    return value

AUGC = [0, 0, 0, 0]
for base in RNA_seq:
    if base == 'A':
        AUGC[0] += 1
    elif base == 'U':
        AUGC[1] += 1
    elif base == 'G':
        AUGC[2] += 1
    else:
        AUGC[3] += 1
AU = permutation(max(AUGC[0], AUGC[1]), min(AUGC[0], AUGC[1]))
GC = permutation(max(AUGC[2], AUGC[3]), min(AUGC[2], AUGC[3]))

print (AU*GC)
