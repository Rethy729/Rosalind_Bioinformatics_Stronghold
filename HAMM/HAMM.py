s = input()
t = input()

h_d = 0
for i in range (0, len(s)):
    if s[i] != t[i]:
        h_d = h_d+1

print (h_d)
    
