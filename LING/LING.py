from numpy.ma.core import subtract

f = open('rosalind_ling.txt', 'r')
data = f.readlines()
text = data[0].strip()
#print(text)

def suffix_array(text):
    suffix_lst = []
    suffix_dict = {}

    for i in range(len(text)):
        suffix_lst.append(text[i:])
        suffix_dict[text[i:]] = i

    sorted_suffix_lst = sorted(suffix_lst)
    suffix_array = []
    for suffix in sorted_suffix_lst:
        suffix_array.append(suffix_dict[suffix])
    return suffix_array

suffix_array = suffix_array(text)

def all_common_prefix(text, suffix_array):
    #common_prefix_lst = []
    common_count = 0
    for i in range(1, len(text)):
        suffix_1 = text[suffix_array[i]:]
        suffix_2 = text[suffix_array[i-1]:]
        h = 0
        #common_prefix = ''
        while h<len(suffix_1) and h<len(suffix_2) and suffix_1[h] == suffix_2[h]:
            #common_prefix += suffix_1[h]
            common_count += 1
            #common_prefix_lst.append(common_prefix)
            h += 1

        #if common_prefix != '':
            #common_prefix_lst.append(common_prefix)
    return common_count

common_count = all_common_prefix(text, suffix_array)
#print (common_count)
def ling(text, common_count):
    n = len(text)
    total = 0
    total_p = 0
    for i in range(1, n+1):
        a = n-i+1
        b = 4**i
        total += min(a, b)
        total_p += i
    return (total_p-common_count)/total

print (ling(text, common_count))