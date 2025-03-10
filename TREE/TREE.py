data = open('rosalind_tree.txt', 'r')
rawdata = data.read()
rawdata_1 = rawdata.split('\n')
vertice = int(rawdata_1[0])
edge_raw = rawdata_1[1:-1]
edge = []
for pair in edge_raw:
    edge.append(list(map(int, pair.split(' '))))


graph = {i+1:[] for i in range(vertice)}

for pair in edge:
    graph[pair[0]].append(pair[1])
    graph[pair[1]].append(pair[0])

def dfs(cc, v, visited): #explore the graph and find all the nodes that are connected to the node v
    visited[v] = True #mark the node v as visited
    cc.append(v) #add v to the current connected component
    for i in graph[v]: #for nodes which is connected with node v
        if visited[i] == False: #for nodes which is not visited
            cc = dfs(cc, i, visited) #recursively operate [dfs] with the node i
    return cc

visited = [False for i in range(vertice+1)] #list visited keeps track of whether each node has been visited during the DFS traversal
connected_components = []

for v in range(1, int(vertice)+1):
    if visited[v] == False: #for non-visited nodes starting from 1~~
        cc = [] #temp cc for every loop of for, cc is the whole tree connected with c
        connected_components.append(dfs(cc, v, visited))

print(len(connected_components)-1)
