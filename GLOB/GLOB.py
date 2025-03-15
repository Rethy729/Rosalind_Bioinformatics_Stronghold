f = open('BLOSUM62.txt', 'r')
data = f.readlines()
char_lst = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y','-']
BLOSUM62 = []
for line in data[1:]:
    BLOSUM62.append(list(map(int, line.split())))
#print (BLOSUM62)

f = open('rosalind_glob.txt', 'r')
data = f.readlines()
string_1 = (list(map(str, data[1].strip())))
string_2 = (list(map(str, data[3].strip())))

indel = -5 #score of indel

def matrix_maker(str1, str2, score): #str1 is horizontal, str2 is vertical
    diago = []

    for i in range(len(str2)):
        diago_row = []
        char_2 = str2[i]
        char_2_index = char_lst.index(char_2)
        for j in range(len(str1)):
            char_1 = str1[j]
            char_1_index = char_lst.index(char_1)
            diago_row.append(score[char_1_index][char_2_index])
        diago.append(diago_row)

    return diago

diago = matrix_maker(string_1, string_2, BLOSUM62)

def DP(diago):
    n = len(diago[0])+1 #the horizontal length of the matrix
    m = len(diago)+1 #the vertical length of the matrix
    score_matrix = []

    for i in range(m):
        score_matrix.append([-99999999]*n)

    for i in range(n):
        score_matrix[0][i] = (indel)*i

    for i in range(m):
        score_matrix[i][0] = (indel)*i

    for i in range(1, m):
        for j in range(1, n):
            score_matrix[i][j] = max(score_matrix[i-1][j]+indel, score_matrix[i][j-1]+indel, score_matrix[i-1][j-1]+diago[i-1][j-1])

    return score_matrix

print(DP(diago)[-1][-1])