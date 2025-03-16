f = open("rosalind_rnas.txt", 'r')
seq = f.readlines()[0].strip()

complement = {'A': ['U'], 'U': ['A', 'G'], 'G': ['C', 'U'], 'C': ['G']}

memo = {}
def RNA_secondary(RNA, start, end): # 0-based indexing
    if start >= end or start >= len(RNA) or end < 0:
        return 1

    if (start, end) in memo:
        return memo[(start, end)]
    else:
        pivot = RNA[start]
        target = complement[pivot]
        case_count = 0
        case_count += RNA_secondary(RNA, start+1, end)
        for i in range(start+4, end+1):
            if RNA[i] in target:
                left = RNA_secondary(RNA, start+1, i-1)
                right = RNA_secondary(RNA, i+1, end)
                case_count += (left * right)
    memo[(start, end)] = case_count
    return case_count

print(RNA_secondary(seq, 0, len(seq) - 1))