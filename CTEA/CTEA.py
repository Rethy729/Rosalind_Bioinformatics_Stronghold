f = open('rosalind_ctea.txt', 'r')
data = f.readlines()
string_1 = data[1].strip()
string_2 = data[3].strip()
#the input file has to be 4 lines

#print (string_1)
#print (string_2)
def edit_distance(str2, str1):

    mod = 2**27 - 1
    seq1 = 'X' + str1
    seq2 = 'X' + str2
    n = len(seq1)
    m = len(seq2)
    count = []
    matrix = []
    for i in range(m):
        matrix.append([0] * n)
        count.append([0] * n)
    for i in range(m):
        matrix[i][0] = i
        count[i][0] = 1
    for i in range(n):
        matrix[0][i] = i
        count[0][i] = 1

    for i in range(1, m):
        for j in range(1, n):
            if seq1[j] == seq2[i]:
                matrix[i][j] = matrix[i-1][j-1]
                count[i][j] = count[i-1][j-1]
            else:
                matrix[i][j] = 1 + min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])

            if matrix[i][j] == matrix[i-1][j] + 1:
                count[i][j] += count[i-1][j]
            if matrix[i][j] == matrix[i][j-1] + 1:
                count[i][j] += count[i][j-1]
            if matrix[i][j] == matrix[i-1][j-1] + 1:
                count[i][j] += count[i-1][j-1]

            count[i][j] = count[i][j] % mod

    return count[-1][-1]

count = edit_distance(string_1, string_2)
print (count)