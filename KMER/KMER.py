data = open('rosalind_kmer.txt', 'r')
rawdata = data.read()
rawdata_replace = rawdata.replace("\n", '')
data = rawdata_replace[14:]

lex_order = "ACGT"

def generating_ACGT(num):
    
    lex_list = []
    if num == 1:
        return list(lex_order)
    
    for base in lex_order:
        for strand in generating_ACGT(num-1):
            lex_list.append(base+strand)

    return lex_list

def counting(strand):
    
    four_mer_list = (generating_ACGT(4))
    count = [0] * 256

    for i in range(len(strand)-3):
        idx = four_mer_list.index(strand[i:i+4])
        count[idx] += 1

    return count

print(" ".join(map(str, counting(data))))

