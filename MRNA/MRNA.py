s = input()

aa = {1:'MW', 2:'FYHQNKDEC', 3:'I', 4:'VPTAG', 6:'LRS'}

output = 1

for letter in s:
    
    if letter in aa[1]:
        output = output
    if letter in aa[2]:
        output = output*2
    if letter in aa[3]:
        output = output*3
    if letter in aa[4]:
        output = output*4
    if letter in aa[6]:
        output = output*6
        
    if output>1000000:
        output = output%1000000
        
print ((output*3)%1000000)

