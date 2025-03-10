f = open("rosalind_kmp.txt", 'r')
raw_data = f.read()
data = raw_data.split('>Rosalind_')
data = data[1:]
DNA_seq = data[0][4:].replace('\n', '')

n = len(DNA_seq)
failure_array = [0] * n

j = 0
for i in range(1, n):

    while j > 0 and DNA_seq[j] != DNA_seq[i]:
        j = failure_array[j-1]
    
    if DNA_seq[i] == DNA_seq[j]:
        j += 1

    failure_array[i] = j

w = open('output_kmp.txt', 'w')
w.write(' '.join(map(str, failure_array)))
w.close()

