memo = {1:[1, 0], 2:[0, 1]}

def rabbit(n,k):

    if n in memo:
        return memo[n]

    #main
    immortal_rabbit = [0,0]
    immortal_rabbit[0] = (k)*(rabbit(n-1, k)[1])
    immortal_rabbit[1] = rabbit(n-1, k)[0] + rabbit(n-1, k)[1]

    memo[n] = immortal_rabbit

    return immortal_rabbit

n = int(input())
k = int(input())
rab = rabbit(n, k)
answer = rab[0]+rab[1]
print (answer)
