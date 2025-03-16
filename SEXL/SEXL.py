f = open('rosalind_sexl.txt', 'r')
data = list(map(float, f.readlines()[0].strip().split()))
print (data)

B = []

for n in data:
    B.append(round(2*n*(1-n), 3))

print (' '.join(map(str, B)))