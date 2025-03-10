s = input()

a = 0
t = 0
g = 0
c = 0

for i in s:
        if i == 'A':
            a = a+1
        if i == 'T':
            t = t+1
        if i == 'G':
            g = g+1
        if i == 'C':
            c = c+1
print (a, c, g, t)

