import math

f = open('rosalind_indc.txt', 'r')
data = f.readlines()
n = int(data[0].strip())

p = 0.5

p_k = 0
answer = []
for k in range(2*n, 0, -1):
    p_k += math.factorial(2*n)/(math.factorial(k)*math.factorial(2*n-k))*(p**k)*((1-p)**(2*n-k))
    answer.append(round(math.log10(p_k), 3))

print(' '.join(map(str, answer[::-1])))