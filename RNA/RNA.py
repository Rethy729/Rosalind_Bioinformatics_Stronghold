seq = input()
seq_split = list(seq)
"""print seq_split"""
i = 0
for base in seq_split:
        if base == 'T':
            seq_split[i] = 'U'
        i = i+1
seq_transcription = "".join(seq_split)
print (seq_transcription)

        
 
