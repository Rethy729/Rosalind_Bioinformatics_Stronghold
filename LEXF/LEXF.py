s = input()
n = int(input())
def merge(string):
    return string.replace(' ', '')

def lex(num):
    lex_list = []
    
    if num == 1:
        return list(merge(s))
    
    for lex_order in merge(s):
        for strand in lex(num-1):
            lex_list.append(lex_order+strand)

    return lex_list

for i in lex(n):
    print (i)
