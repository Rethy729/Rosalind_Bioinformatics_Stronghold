amino_acid = {('TAA', 'TAG', 'TGA'): 'X', ('TTT', 'TTC'):'F', ('TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'):'L', ('ATT', 'ATC', 'ATA'):'I', ('ATG'):'M', ('GTT', 'GTC', 'GTA', 'GTG'):'V', ('TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'):'S',('CCT', 'CCC', 'CCA', 'CCG'):'P', ('ACT', 'ACC', 'ACA', 'ACG'):'T', ('GCT', 'GCC', 'GCA', 'GCG'):'A', ('TAT', 'TAC'):'Y', ('CAT', 'CAC'):'H', ('CAA', 'CAG'):'Q', ('AAT', 'AAC'):'N', ('AAA', 'AAG'):'K', ('GAT', 'GAC'):'D', ('GAA', 'GAG'):'E',('TGT', 'TGC'):'C', ('TGG'):'W', ('CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'):'R', ('GGT', 'GGC', 'GGA', 'GGG'):'G'}

f = open('rosalind_SPLC.txt', 'r')
data = f.readlines()

RNA_seq = []
for i in range(len(data)):
    if i%2 == 1:
        RNA_seq.append(data[i].strip())

def splicing(base_list):
    for i in range(1, len(base_list)):
        index = base_list[0].find(base_list[i])
        base_list[0] = base_list[0][:index]+base_list[0][index+len(base_list[i]):]

    return base_list[0]

def translation(strand):
    protein = ''
    for i in range(0, len(strand)-2, 3):
        codon = strand[i:i+3]
        for key in amino_acid:
            if codon in key:
                protein = protein + amino_acid[key]
    return protein[:-1]

print(translation(splicing(RNA_seq)))
