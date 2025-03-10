s = input()
t = input()

def findme(lst1, lst2):
    len_lst1 = len(lst1)
    len_lst2 = len(lst2)
    find = []
    for i in range (0, (len_lst1-len_lst2+1)):
        key = 0
        for j in range(0, len_lst2):
            if lst1[i+j]==lst2[j]:
                key = key+1   
        if key == len_lst2:
            find.append(i+1)
    return find

result = findme(s, t)
for i in range(len(result)):
    result[i] = str(result[i])
print(' '.join(result))
