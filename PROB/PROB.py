import math

def prob_cal(strand, gc):
    odd = 1
    for base in strand:
        if base == 'G' or base == 'C':
            odd = odd*(gc/2)
        if base == 'A' or base == 'T':
            odd = odd*((1-gc)/2)

    return math.log10(odd)

s = input()
gc = input()

split_gc = gc.split(' ')
result = []
for gc in split_gc:
    result.append(prob_cal(s,float(gc)))
    
print (' '.join(map(str, result)))
