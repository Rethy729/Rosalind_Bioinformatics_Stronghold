
f = open("rosalind_corr.txt", 'r')
raw_data = f.read()
data = raw_data.split('>Rosalind_')
data = data[1:]
DNA_seq = []
for line in data:
    DNA_seq.append(line[4:].replace('\n', ''))

complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

def HD(seq1, seq2):
    HD = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            HD += 1
    return HD

def comp(seq):
    comp_seq = ''
    for base in seq:
        comp_seq = complement[base] + comp_seq
    return comp_seq

def correct_read(DNA_seq):
    #returns "correct_read" and remove them from DNA_seq list
    correct_read = set()
    for i in range(len(DNA_seq)):
        count = 0
        for j in range(len(DNA_seq)):
            if DNA_seq[i] == DNA_seq[j] or comp(DNA_seq[i]) == DNA_seq[j]:
                count += 1
        if count >= 2:
            correct_read.add(DNA_seq[i])
            correct_read.add(comp(DNA_seq[i]))
    return correct_read

def match(DNA_seq, correct_set):
    match = []
    for seq in DNA_seq:
        if seq not in correct_set:
            for seq_corr in correct_set:
                if HD(seq, seq_corr) == 1:
                    match.append([seq, seq_corr])
                    break
        else:
            continue
    return match

answer = match(DNA_seq, correct_read(DNA_seq))
w = open('output_corr.txt', 'w')
for pair in answer:
    w.write(pair[0]+'->'+pair[1]+'\n')
w.close()
