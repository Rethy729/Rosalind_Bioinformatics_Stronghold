memo = {1:1}

def factorial(n):
    
    if n in memo:
        return memo[n]
    value = n*factorial(n-1)
    memo[n] = value
    return value

def CountATGC(strand):
    a = 0
    g = 0
    for base in strand:
        if base == 'A':
            a += 1
        if base == 'G':
            g += 1
    return factorial(a) * factorial (g)

s = input()
print (CountATGC(s))
