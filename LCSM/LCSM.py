f = open("rosalind_lcsm.txt", 'r')
raw_data = f.read()
data = raw_data.split('>Rosalind_')
data = data[1:]
DNA_seq = []
for line in data:
    DNA_seq.append(line[4:].replace('\n', ''))

def find_common_string(seq1, seq2):

    if len(seq2)>len(seq1):
        seq1, seq2 = seq2, seq1

    n = len(seq2)

    for i in range(n):
        for j in range(i+1):
            sub_string = seq2[j:j+(n-i)]
            if sub_string in seq1:
                return sub_string

def find_longest_common_string(lst):
    common = ''
    for i in range(len(lst)-1):
        if common == '':
            common = find_common_string(lst[i], lst[i+1])

        else:
            if len(common) >= len(find_common_string(lst[i+1], common)):
                common = find_common_string(lst[i+1], common)
    return common

import time

start_time = time.time()
print (find_longest_common_string(DNA_seq))
end_time = time.time()
print(end_time - start_time)
