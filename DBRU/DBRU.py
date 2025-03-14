f = open("rosalind_dbru.txt", 'r')
raw_data = f.read()
data = raw_data.split('\n')[:-1]
k = len(data[0])

comp = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
def reverse_complement(str):
    comp_str = ''
    for base in str:
        comp_str = comp[base] + comp_str
    return comp_str

data_set = set(data)
rev_data_set = set()
for string in set(data):
    rev_data_set.add(reverse_complement(string))
data_set = list(data_set | rev_data_set)

DeBruijn = {}
for i in range(len(data_set)):
    sub_text = data_set[i]
    print ('('+str(sub_text[:-1])+', '+str(sub_text[1:])+')')
