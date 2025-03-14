f = open("rosalind_rear.txt", 'r')
raw_data = f.read()
data = raw_data[:-1].split('\n\n')
perm = []
for string in data:
    perm.append(list(string.split('\n')))

for line in perm:
    line[0] = list(map(int, line[0].split(' ')))
    line[1] = list(map(int, line[1].split(' ')))

def reversal_set(lst): #list -> list in list
    lst_combination = [lst]
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            sub = lst[i:j+1]
            rev = lst[:i] + sub[::-1] + lst[j+1:]
            lst_combination.append(rev)
            
    return lst_combination

def reversal_distance(set1, set2, distance):
    
    if set1 & set2:
        return distance
    
    else:
        new_set_1 = set()
        for perm in set1:
            for comb in reversal_set(list(perm)):
                new_set_1.add(tuple(comb))

        new_set_2 = set()
        for perm in set2:
           for comb in reversal_set(list(perm)):
                new_set_2.add(tuple(comb))

        distance += 2

        if set1 & new_set_2:
            return (distance-1)
        elif set2 & new_set_1:
            return (distance-1)
        else:
            return reversal_distance(new_set_1, new_set_2, distance)
    
for pair in perm:
    set1 = set()
    set2 = set()
    set1.add(tuple(pair[0]))
    set2.add(tuple(pair[1]))
    print(reversal_distance(set1, set2, 0))
