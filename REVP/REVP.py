def reverse(strand):
    comp = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    complement = ''
    for base in strand:
        complement += comp[base]
    return complement[::-1]

def palindrome(strand):
    palindrome = []
    for i in range(4, 13, 2):
        for j in range(len(strand)-i+1):
            if strand[j:j+i] == reverse(strand[j:j+i]):
                palindrome.append([j+1, i])
    return palindrome

    
s = input()

answer = palindrome(s)

for pairs in answer:
    print (pairs[0], pairs[1])
