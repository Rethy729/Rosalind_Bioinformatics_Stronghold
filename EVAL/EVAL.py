f = open('rosalind_eval.txt', 'r')
data = f.readlines()
n = int(data[0])
seq = data[1].strip()
gc = list(map(float, data[2].strip().split()))

print (n)
print (seq)
print (gc)

answer = []

slide = n - len(seq) + 1


for p in gc:
    p_m = 1
    for base in seq:
        if base == 'A' or base == 'T':
           p_m *= (1-p)/2
        else:
            p_m *= p/2
    answer.append(round(slide*p_m, 3))

print (' '.join(map(str, answer)))
