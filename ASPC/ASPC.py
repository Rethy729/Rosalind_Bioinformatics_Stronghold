f = open("rosalind_aspc.txt", 'r')
raw_data = f.read()
data = list(map(int, raw_data.split(' ')))

def combination(n, m):

    if (n-m) >= m:
        top = 1
        for i in range(n, n-m, -1):
            top = top * i
        bottom = 1
        for i in range(m, 0, -1):
            bottom = bottom * i
        return (top/bottom) % 1000000

    else:
        top = 1
        for i in range(n, m, -1):
            top = top * i
        bottom = 1
        for i in range(n-m, 0, -1):
            bottom = bottom * i
        return (top//bottom) % 1000000

def sigma(n, m):
    summ = 0
    for k in range(n , m-1, -1):
        summ += combination(n, k)
        if summ > 1000000:
            summ = summ % 1000000
    return summ

print (sigma(data[0], data[1]))
