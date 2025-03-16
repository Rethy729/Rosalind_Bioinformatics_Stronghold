from itertools import product
from collections import defaultdict

f = open("rosalind_conv.txt", 'r')
data = f.readlines()

set_1 = list(map(float, data[0].strip().split()))
set_2 = list(map(float, data[1].strip().split()))

print(set_1)
print(set_2)

def convolution(set_1, set_2):

    convolution_lst = []
    for i in range(len(set_1)):
        for j in range(len(set_2)):
            convolution_lst.append(round(set_1[i] - set_2[j], 5))
    for i, num in enumerate(convolution_lst):
        if num<0:
            convolution_lst[i] = -num
    convolution = defaultdict(int)
    for num in convolution_lst:
        convolution[num] += 1
    maximum = 0
    maximum_num = 0
    for key in convolution:
        if convolution[key] > maximum_num:
            maximum_num = convolution[key]
            maximum = key

    print (maximum_num)
    print(maximum)

convolution(set_1, set_2)