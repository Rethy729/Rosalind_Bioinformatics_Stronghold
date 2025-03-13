from urllib.request import urlopen

f = open('rosalind_mprt.txt', 'r')
data = f.readlines()

for i in range(len(data)):
    data[i] = data[i].strip()
for id in data:

    uniprot_id = id.split('_')[0]
    url = f"http://www.uniprot.org/uniprot/{uniprot_id}.fasta"
    protein_download = urlopen(url)
    protein_data = protein_download.readlines()[1:]
    for i in range(len(protein_data)):
        protein_data[i] = protein_data[i].decode('utf-8').strip()
    protein_fasta = ''.join(protein_data)

    index = []
    for i in range(len(protein_fasta)-3):

        motif = protein_fasta[i:i+4]
        if motif[0] == 'N':
            if motif[1] != 'P':
                if motif[2] == 'S' or motif[2] == 'T':
                    if motif[3] != 'P':
                        index.append(i+1)
    if len(index) == 0:
        continue

    print (id)
    print (' '.join(map(str, index)))
