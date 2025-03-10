memo = {1:1}

def factorial(n):
    if n in memo:
        return memo[n]
    value = n*factorial(n-1)
    memo[n] = value
    return value

n = int(input())
m = int(input())

print ((factorial(n)//factorial(n-m))%1000000)
