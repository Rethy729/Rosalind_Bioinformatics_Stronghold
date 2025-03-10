n = input()
m = input()

def indices(template, sub):
    indices = [0]*len(sub)
    
    for i in range(len(sub)):
        for j in range(len(template)):
            if sub[i] == template[j] and indices[i-1]<j:
                indices[i] = j
                break
    return indices

indices_final = []
for num in indices(n, m):
    indices_final.append(num+1)

print(' '.join(map(str, indices_final)))
                
