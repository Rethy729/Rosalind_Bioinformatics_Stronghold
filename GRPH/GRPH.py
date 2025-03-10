data = open('rosalind_grph.txt', 'r')
rawdata = data.read()
rawdata_split = rawdata.split('>')
rawdata_r = rawdata_split[1:]

sequence = []
index = []
for sets in rawdata_r:
    
    setss = sets[14:].replace("\n", "")
    indexx = sets[9:13]
    
    sequence.append(setss)
    index.append(indexx)

suffix = []
prefix = []

for seq in sequence:
    suffix.append(seq[-3:])
    prefix.append(seq[:3])

for i in range(len(suffix)):
    for j in range(len(prefix)):
        if suffix[i] == prefix[j] and sequence[i] != sequence[j]:
            a = index[i]
            b = index[j]
            print ("Rosalind_"+a+" "+"Rosalind_"+b)

