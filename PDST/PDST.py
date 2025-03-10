f = open("rosalind_pdst.txt", 'r')
raw_data = f.read()
data = raw_data.split('>Rosalind_')
data = data[1:]
DNA_seq = []
for line in data:
    DNA_seq.append(line[4:].replace('\n', ''))

def Distance(seq1, seq2):
    l = len(seq1)
    dist = 0
    for i in range(l):
        if seq1[i] != seq2[i]:
            dist += 1
    return round(float(dist)/l, 5)

def DistanceMatrix(lst):
    n = len(lst)
    matrix = []
    for i in range(n):
        matrix.append([0]*n)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j] = Distance(lst[i], lst[j])
            matrix[j][i] = matrix[i][j]
    return matrix

w = open('output_pdst.txt', 'w')
for row in DistanceMatrix(DNA_seq):
    w.write(' '.join(map(str, row))+'\n')
w.close()

