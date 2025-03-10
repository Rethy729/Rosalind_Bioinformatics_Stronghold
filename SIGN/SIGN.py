def signed_permutation(n):
    if n == 1:
        return [['1'], ['-1']]

    perm_list = []
    plus = [str(n)]
    minus = [str(-n)]
    for number_lists in signed_permutation(n-1):
        for i in range(n):
            f = number_lists[:i]
            b = number_lists[i:]
            
            new_1 = f + plus + b
            new_2 = f + minus + b
            perm_list.append(new_1)
            perm_list.append(new_2)
    return perm_list


n = int(input())
print(len(signed_permutation(n)))
permutation = signed_permutation(n)
for i in permutation:
    result = " ".join(i)
    print(result)
