data = open('rosalind_gc.txt', 'r')
rawdata = data.read()
rawdata_split = rawdata.split('>')
rawdata_r = rawdata_split[1:]
gc = {}
for rosalind in rawdata_r:
    index = rosalind[9:13]
    raw_sequence = rosalind[14:]
    sequence = raw_sequence.replace('\n', '')

    i=0
    j=0
    for base in sequence:
        if base == 'G' or base == 'C':
            i=i+1
            j=j+1
        if base == 'A' or base == 'T':
            i = i+1
        ratio = j/i
        gc[index] = round(ratio, 5)
            
sorted_gc = sorted(gc.items(), key = lambda item:item[1], reverse=True)

print ("Rosalind_" + sorted_gc[0][0])
print (sorted_gc[0][1] *100)