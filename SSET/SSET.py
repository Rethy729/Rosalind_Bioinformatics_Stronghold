
n = int(input())
'''
def subset(n):
    if n == 1:
        return 2
    else:
        return (subset(n-1)*2)%1000000

print subset(n)
'''
def subset(n):
    result = 2 
    for i in range(2, n + 1):
        result = (result * 2) % 1000000
    return result

print(subset(n))
