f = open("rosalind_motz.txt", 'r')
raw_data = f.read()
RNA_strand = raw_data[14:].replace('\n', '')
print (RNA_strand)

complement = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G'}

memo = {}
def RNA_secondary(RNA, start, end):  # 0-based indexing

    if start >= end or start >= len(RNA) or end < 0:
        return 1

    if (start, end) in memo:
        return memo[(start, end)]
    else:
        pivot = RNA[start]
        target = complement[pivot]
        case_count = 0
        case_count += RNA_secondary(RNA, start+1, end) #different from CAT -> we have to add when start node doesn`t participate in the graph
        for i in range(start + 1, end + 1):            #different from CAT -> we dont have to iterate +2, since it is MOTZKIN!
            if RNA[i] == target:
                left = RNA_secondary(RNA, start + 1, i - 1)
                right = RNA_secondary(RNA, i + 1, end)
                case_count += (left * right) % 1000000

        memo[(start, end)] = case_count
        return case_count

print(RNA_secondary(RNA_strand, 0, len(RNA_strand) - 1) % 1000000)