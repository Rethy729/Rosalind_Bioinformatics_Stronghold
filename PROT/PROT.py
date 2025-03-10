s = input()
n = len(s)
split_data = []
for i in range(0, n//3):
    split_data.append(s[3*i:3*i+3])

protein = ""
def ribosome(lst):
    global protein
    for codon in lst:
        if codon[0] == 'U':
            if codon[1] == 'U':
                if codon[2] == 'U' or codon[2] == 'C':
                    protein = protein + 'F'
                else:
                    protein = protein + 'L'
            if codon[1] == 'C':
                protein = protein + 'S'
            if codon[1] == 'A':
                if codon[2] == 'U' or codon[2] == 'C':
                    protein = protein + 'Y'
                else:
                    return protein
            if codon[1] == 'G':
                if codon[2] == 'U' or codon[2] == 'C':
                    protein = protein + 'C'
                elif codon[2] == 'G':
                    protein = protein + 'W'
                else:
                    return protein
                
        if codon[0] == 'C':
            if codon[1] == 'U':
                protein = protein + 'L'
            if codon[1] == 'C':
                protein = protein + 'P'
            if codon[1] == 'A':
                if codon[2] == 'U' or codon[2] == 'C':
                    protein = protein + 'H'
                else:
                    protein = protein + 'Q'
            if codon[1] == 'G':
                protein = protein + 'R'
                
        if codon[0] == 'A':
            if codon[1] == 'U':
                if codon[2] == 'G':
                    protein = protein + 'M'
                else:
                    protein = protein + 'I'
            if codon[1] == 'C':
                protein = protein + 'T'
            if codon[1] == 'A':
                if codon[2] == 'U' or codon[2] == 'C':
                    protein = protein + 'N'
                else:
                    protein = protein + 'K'
            if codon[1] == 'G':
                if codon[2] == 'U' or codon[2] == 'C':
                    protein = protein + 'S'
                else:
                    protein = protein + 'R'

        if codon[0] == 'G':
            if codon[1] == 'U':
                protein = protein + 'V'
            if codon[1] == 'C':
                protein = protein + 'A'
            if codon[1] == 'A':
                if codon[2] == 'U' or codon[2] == 'C':
                    protein = protein + 'D'
                else:
                    protein = protein + 'E'
            if codon[1] == 'G':
                protein = protein + 'G'
                    
print(ribosome(split_data))
