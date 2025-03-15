f = open('rosalind_edta.txt', 'r')
data = f.readlines()
string_1 = data[1].strip()
string_2 = data[3].strip()
#the input file has to be 4 lines

#print (string_1)
#print (string_2)
def edit_distance(str1, str2):
    seq1 = 'X' + str1
    seq2 = 'X' + str2
    n = len(seq1)
    m = len(seq2)

    matrix = []
    for i in range(m):
        matrix.append([0] * n)

    for i in range(m):
        matrix[i][0] = i
    for i in range(n):
        matrix[0][i] = i

    for i in range(1, m):
        for j in range(1, n):
            if seq1[j] == seq2[i]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = 1 + min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])

    return matrix
matrix = edit_distance(string_1, string_2)

indel = 1

def Backtracking(score):
    route = ''
    sii = len(score)-1 #sii = start_index_i
    sij = len(score[0])-1 #sij = start_index_j

    while sii != 0 and sij != 0:
        if score[sii][sij] == score[sii-1][sij] + indel:
            route = 'd' + route
            sii = sii - 1
        elif score[sii][sij] == score[sii][sij-1] + indel:
            route = 'i' + route
            sij = sij - 1
        else:
            route = 'm' + route
            sii = sii - 1
            sij = sij - 1
    for i in range(sii):
        route = 'd' + route
    for i in range(sij):
        route = 'i' + route

    return route

route = Backtracking(matrix)

def route_to_alignment(str1, str2, route): #str1 is horizontal, str2 is vertical
    align_str1 = ''
    align_str2 = ''
    index_1 = 0
    index_2 = 0
    for path in route:
        if path == 'm':
            align_str1 += str1[index_1]
            align_str2 += str2[index_2]
            index_1 += 1
            index_2 += 1
        elif path == 'i':
            align_str1 += str1[index_1]
            align_str2 += '-'
            index_1 += 1
        else:
            align_str1 += '-'
            align_str2 += str2[index_2]
            index_2 += 1
    print (align_str1)
    print (align_str2)

print (matrix[-1][-1])
route_to_alignment(string_1, string_2, route)