amino_acid = {('TAA', 'TAG', 'TGA'): 'X', ('TTT', 'TTC'):'F', ('TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'):'L', ('ATT', 'ATC', 'ATA'):'I', ('ATG'):'M', ('GTT', 'GTC', 'GTA', 'GTG'):'V', ('TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'):'S',('CCT', 'CCC', 'CCA', 'CCG'):'P', ('ACT', 'ACC', 'ACA', 'ACG'):'T', ('GCT', 'GCC', 'GCA', 'GCG'):'A', ('TAT', 'TAC'):'Y', ('CAT', 'CAC'):'H', ('CAA', 'CAG'):'Q', ('AAT', 'AAC'):'N', ('AAA', 'AAG'):'K', ('GAT', 'GAC'):'D', ('GAA', 'GAG'):'E',('TGT', 'TGC'):'C', ('TGG'):'W', ('CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'):'R', ('GGT', 'GGC', 'GGA', 'GGG'):'G'}

def translation(strand):
    comp = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    complement = ''
    for base in strand:
        complement += comp[base]
       
    strands = [strand, complement[::-1]]
    
    protein_set = []
    for frame in strands:
        for i in range(3):
            protein = ''
            for j in range(i, len(frame)-2, 3):
                codon = frame[j:j+3]
                for key in amino_acid:
                    if codon in key:
                        protein = protein + amino_acid[key]
            protein_set.append(protein)
        
    return protein_set

def possible_protein(ORFlist):
    protein_set = set()
    for frame in ORFlist:
        start = []
        end = []
        for i in range(len(frame)):
            if frame[i] == 'M':
                start.append(i)
            if frame[i] == 'X':
                end.append(i)
        if len(start) ==0 or len(end) ==0:
            continue

        for i in range(len(start)):
            for j in range(len(end)):
                if start[i]<end[j]:
                    protein_set.add(frame[start[i]:end[j]])
                    break
    return protein_set
    

s = input()
ORF = translation(s)
protein_set = possible_protein(ORF)

for i in protein_set:
    print (i)
