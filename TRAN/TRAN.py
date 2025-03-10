
def main_function(strand1, strand2):
    l = len(strand1)
    transition = 0
    transversion = 0
    ideal = 0
    for i in range(l):
        if (strand1[i] == 'A' and strand2[i] == 'G') or (strand1[i] == 'G' and strand2[i] == 'A') or (strand1[i] == 'C' and strand2[i] == 'T') or (strand1[i] == 'T' and strand2[i] == 'C'):
            transition += 1
        elif strand1[i] != strand2[i]:
            transversion += 1
        else:
            ideal += 1
    
    return float(transition)/float(transversion)

m = input()
n = input()
print(main_function(m, n))
