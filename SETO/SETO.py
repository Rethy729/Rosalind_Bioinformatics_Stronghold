f = open("rosalind_seto.txt", 'r')
raw_data = f.read()
data = raw_data.split('\n')

whole = set()
n = int(data[0])

for i in range(1, n+1):
    whole.add(i)

list_a = list(map(int, data[1][1:-1].split(', ')))
list_b = list(map(int, data[2][1:-1].split(', ')))

set_a = set(list_a)
set_b = set(list_b)

w = open('output_seto.txt', 'w')
w.write("{" + ", ".join(map(str, (set_a|set_b))) + "}" + "\n")
w.write("{" + ", ".join(map(str, (set_a&set_b))) + "}" + "\n")
w.write("{" + ", ".join(map(str, (set_a-set_b))) + "}" + "\n")
w.write("{" + ", ".join(map(str, (set_b-set_a))) + "}" + "\n")
w.write("{" + ", ".join(map(str, (whole-set_a))) + "}" + "\n")
w.write("{" + ", ".join(map(str, (whole-set_b))) + "}")
w.close()
