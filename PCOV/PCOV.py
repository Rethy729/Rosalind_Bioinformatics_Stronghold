f = open("rosalind_pcov.txt", 'r')
raw_data = f.read()
data = raw_data.split('\n')[:-1]
kmers = data[:]

def make_graph(kmers):
    graph = {}
    for kmer in kmers:
        if kmer in graph:
            continue
        else:
            graph[kmer] = []

    for key in graph:
        for kmer in kmers:
            if key[1:] == kmer[:-1]:
                graph[key].append(kmer)
    return graph

graph_data = make_graph(kmers)
#print (make_graph(kmers))

def find_cycle(start_node, graph):
    cycle = []
    arr_node = graph[start_node].pop()

    while arr_node != start_node:
        cycle.append(arr_node)
        arr_node = graph[arr_node].pop()
    cycle.append(arr_node)

    for key in list(graph):
        if graph[key] == []:
            del graph[key]

    return cycle


def EulerianCycle(start_node, graph):
    cycle = [start_node] + find_cycle(start_node, graph)

    break_bool = True
    while break_bool:
        break_bool = False
        for i, node in enumerate(cycle):
            if node in graph:
                break_bool = True
                cycle = cycle[:i+1] + find_cycle(node, graph) + cycle[i+1:]
                break

    return cycle

cycle = EulerianCycle(kmers[0], graph_data)

def CycleToString(cycle, k):
    kmer = []
    for i in range(len(cycle)-1):
        kmer.append(cycle[i]+cycle[i+1][-1])
    cycle_string = kmer[0]
    for i in range(1, len(kmer)-k+1):
        cycle_string = cycle_string + kmer[i][-1]
    return cycle_string

print (CycleToString(cycle, len(kmers[0])+1))