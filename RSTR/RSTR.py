f = open("rosalind_rstr.txt", 'r')
raw_data = f.read()
data = raw_data.split('\n')
num_data = [int(data[0].split()[0]), float(data[0].split()[1])]
DNA_seq = data[1]

odds = {'G':(num_data[1]/2), 'C':(num_data[1]/2), 'A':(1-num_data[1])/2, 'T':(1-num_data[1])/2}

def build_string(DNA_seq, n):
    
    prob = 1
    for base in DNA_seq:
        prob = prob*odds[base]

    prob_c = 1-prob

    prob_2 = 1
    for i in range(n):
        prob_2 = prob_2 * prob_c

    return round(1-prob_2, 3)

print (build_string(DNA_seq, num_data[0]))
