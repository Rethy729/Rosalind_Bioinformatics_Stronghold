def matrix(lst):
    matrix = []
    n = len(lst[0])
    for i in range(n):
        temp_list = [0, 0, 0, 0]
        for seq in lst:
            
            if seq[i] == 'A':
                temp_list[0] = temp_list[0]+1
            if seq[i] == 'C':
                temp_list[1] = temp_list[1]+1
            if seq[i] == 'G':
                temp_list[2] = temp_list[2]+1
            if seq[i] == 'T':
                temp_list[3] = temp_list[3]+1
        matrix.append(temp_list)
    return matrix

def consensus(lst):

    consensus = ""
    for sublist in lst:
        if sublist.index(max(sublist)) == 0:
            consensus = consensus + 'A'
        if sublist.index(max(sublist)) == 1:
            consensus = consensus + 'C'
        if sublist.index(max(sublist)) == 2:
            consensus = consensus + 'G'
        if sublist.index(max(sublist)) == 3:
            consensus = consensus + 'T'

    return consensus


def transpose(lst):
    matrix_transpose = [[],[],[],[]]
    for i in range(4):
        for sublist in lst:
            matrix_transpose[i].append(sublist[i])
            
    a = ' '.join(map(str, matrix_transpose[0]))
    c = ' '.join(map(str, matrix_transpose[1]))
    g = ' '.join(map(str, matrix_transpose[2]))
    t = ' '.join(map(str, matrix_transpose[3]))
    
    print ("A: "+a)
    print ("C: "+c)
    print ("G: "+g)
    print ("T: "+t)

data = open('rosalind_cons.txt', 'r')
rawdata = data.read()
rawdata_split = rawdata.split('>')
rawdata_r = rawdata_split[1:]

sequences = []
for sets in rawdata_r:
    setss = sets[14:].replace("\n", "")
    sequences.append(setss)
    
#print(matrix(sequences))
print(consensus(matrix(sequences)))
transpose(matrix(sequences))

