def permutation(n):
    if n==1:
        return ['1']

    perm_list = []
    for numbers in permutation(n-1):
        for i in range(n):
            f = numbers[:i]
            b = numbers[i:]
            new = f + str(n) + b
            perm_list.append(new)
    return perm_list

n = int(input())
print(len(permutation(n)))
permutation = permutation(n)
for i in permutation:
    result = " ".join(i)
    print(result)

