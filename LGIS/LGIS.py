f = open("rosalind_lgis.txt", 'r')
raw_data = f.read()
data = raw_data.split('\n')
n = int(data[0])
sequence = list(map(int, data[1].split(' ')))

def LGIS(sequence, n):

    route = [1] * n
    backtrack = [-1] * n

    for i in range(n):
        for j in range(i):
            if sequence[i] > sequence[j] and route[j]+1 > route[i]:
                route[i] = route[j] + 1
                backtrack[i] = j

    lgis_len = max(route)
    lgis = []
    track_index = route.index(lgis_len)
    print (backtrack)
    while track_index != -1:
        lgis.append(sequence[track_index])
        track_index = backtrack[track_index]
    print (lgis[::-1])
    return lgis[::-1]

def LGDS(sequence, n):

    route = [1] * n
    backtrack = [-1] * n

    for i in range(n):
        for j in range(i):
            if sequence[i] < sequence[j] and route[j]+1 > route[i]:
                route[i] = route[j] + 1
                backtrack[i] = j

    lgis_len = max(route)
    lgis = []
    track_index = route.index(lgis_len)
    
    while track_index != -1:
        lgis.append(sequence[track_index])
        track_index = backtrack[track_index]

    return lgis[::-1]

w = open('output_lgis.txt', 'w')
w.write(' '.join(map(str, LGIS(sequence, n)))+'\n')
w.write(' '.join(map(str, LGDS(sequence, n))))
w.close()
