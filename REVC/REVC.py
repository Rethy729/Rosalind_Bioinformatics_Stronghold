s = input()
s_c_rev = ""
s_c = ""
s_list = list(s)


for base in s_list:
        if base == 'A':
            s_c_rev = s_c_rev + 'T'
        if base == 'T':
            s_c_rev = s_c_rev + 'A'
        if base == 'G':
            s_c_rev = s_c_rev + 'C'
        if base == 'C':
            s_c_rev = s_c_rev + 'G'


for base in s_c_rev:
    s_c = base + s_c

print (s_c)
    
