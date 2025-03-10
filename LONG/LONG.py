f = open("rosalind_long.txt", 'r')
raw_data = f.read()
data = raw_data.split('>Rosalind_')
data = data[1:]
DNA_string = []
for i in range(len(data)):
    DNA_string.append(data[i][4:].replace('\n', ''))

def merge_pre(DNA_string):

    break_bool = True

    while break_bool:

        break_bool = False

        pivot = DNA_string[0]
        count = 0

        DNA_string_temp = DNA_string[:] #to prevent list iteration during for loop
        for i in range(1, len(DNA_string_temp)): 
            length = len(DNA_string_temp[i])
            for j in range(length, length//2, -1):
                if pivot[:j] == DNA_string_temp[i][length-j:]:
                    break_bool = True

                    DNA_string[0] = DNA_string[i][:length-j] + pivot
                    DNA_string.remove(DNA_string_temp[i])

                    count += 1
                    break
            if count == 1:
                break
            
    return DNA_string[0]

def merge_pro(DNA_string):

    break_bool = True
    
    while break_bool:
        
        break_bool = False
        
        pivot = DNA_string[0]
        l = len(pivot)
        count = 0
        
        DNA_string_temp = DNA_string[:] 
        for i in range(1, len(DNA_string_temp)):
            length = len(DNA_string_temp[i])
            for j in range(length, length//2, -1):
                if pivot[l-j:] == DNA_string_temp[i][:j]:
                    break_bool = True
                    
                    DNA_string[0] = pivot + DNA_string[i][j:]
                    DNA_string.remove(DNA_string_temp[i])
    
                    count += 1
                    break
                
            if count == 1:
                break
        
    return DNA_string[0]

merge_pro(DNA_string)
merge_pre(DNA_string)

w = open('output_long.txt', 'w')
w.write(DNA_string[0])
w.close()

