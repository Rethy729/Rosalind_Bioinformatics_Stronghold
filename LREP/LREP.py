f = open('rosalind_lrep.txt', 'r')
data = f.readlines()
text = data[0].strip()
#print(text)
k = int(data[1].strip())
#print(k)

def suffix_array(text):
    suffix_lst = []
    suffix_dict = {}

    for i in range(len(text)):
        suffix_lst.append(text[i:])
        suffix_dict[text[i:]] = i

    sorted_suffix_lst = sorted(suffix_lst)
    print (sorted_suffix_lst)
    suffix_array = []
    for suffix in sorted_suffix_lst:
        suffix_array.append(suffix_dict[suffix])
    return suffix_array

suffix_array = suffix_array(text)

def longest_common_prefix(text, suffix_array):
    common_prefix_lst = []
    print (suffix_array)
    for i in range(1, len(text)):
        suffix_1 = text[suffix_array[i]:]
        suffix_2 = text[suffix_array[i-1]:]
        h = 0
        common_prefix = ''
        while h<len(suffix_1) and h<len(suffix_2) and suffix_1[h] == suffix_2[h]:
            common_prefix += suffix_1[h]
            common_prefix_lst.append(common_prefix)
            h += 1
        #if common_prefix != '':
            #common_prefix_lst.append(common_prefix)
    print (common_prefix_lst)

    k_repeats = []
    for sub_string_1 in set(common_prefix_lst):
        count = 0
        for sub_string_2 in common_prefix_lst:
            if sub_string_1 == sub_string_2:
                count += 1
        if count >= k-1:
            k_repeats.append(sub_string_1)
    #print (k_repeats)
    return max(k_repeats, key = len)

print (longest_common_prefix(text, suffix_array))