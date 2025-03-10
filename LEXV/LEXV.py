f = open("rosalind_lexv.txt", 'r')
raw_data = f.read()
data = raw_data.split('\n')
letters = data[0].split()
n = int(data[1])
lex_letters = ['0']+letters
print (lex_letters)

def lex_list(lst, n):
    if n == 1:
        return lst
    lex_lst = []
    for letter in lst:
        for string in lex_list(lst, n-1):
            lex_lst.append(letter+string)
    return lex_lst

def remove(lst, n):
    
    lex_lst = lst[4**(n-1):] #0���� �����ϴ� ���� ����

    lex_lst_temp = lex_lst[:]
    for string in lex_lst:
        for i in range(n-1):
            if string[i] == '0' and string[i+1] != '0': #'0X'�� ���� ���� ����
                lex_lst_temp.remove(string)
    print (lex_lst_temp)

    lex = []
    for i in range(len(lex_lst_temp)): #���ҵ��� ������ �޸� '0' (or '0's)�� ����
        if lex_lst_temp[i][-1] == '0':
            for j in range(n):
                if lex_lst_temp[i][j] == '0':
                    lex.append(lex_lst_temp[i][:j])
                    break
        else:
            lex.append(lex_lst_temp[i])
    return lex

w = open('output_lexv.txt', 'w')
for line in remove(lex_list(lex_letters, n), n):
    w.write(line+'\n')
w.close()

    
