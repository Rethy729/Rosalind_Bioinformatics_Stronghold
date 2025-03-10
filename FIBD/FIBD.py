memo = {1:[1, 0], 2:[0, 1]}

def mortal_rabbit(n,m):

    if n in memo:
        return memo[n]

    #main
    mortal_r = []
    mortal_r.append(mortal_rabbit(n-1, m)[1])
    mortal_r.append(mortal_rabbit(n-1, m)[0] + mortal_rabbit(n-1, m)[1])
    if n-m>=1:
        mortal_r[1] = mortal_r[1] - mortal_rabbit(n-m, m)[0]

    memo[n] = mortal_r
    return mortal_r

n = int(input())
m = int(input())
mortal_rabbit(n, m)
rabbit = memo[n]
print(rabbit[0]+rabbit[1])


