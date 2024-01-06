inputFile=open('input3.txt','r')
f_line=list(map(int,inputFile.readline().split(' ')))
n_vertices,m_edges=f_line[0],f_line[1]
dict1={}
# Representing the graph with Adjacency List
for i in range(m_edges):
    graph=list(map(int,inputFile.readline().split(' ')))
    ver1,ver2=graph
    try:
        dict1[ver1].append(ver2)
    except KeyError:
        dict1[ver1]=[ver2]
    try:
        dict1[ver2].append(ver1)
    except KeyError:
        dict1[ver2]=[ver1]
# DFS Traversal
visited=[1]
stack=[1]
while stack:
    current_vertex=stack.pop()
    if current_vertex not in visited:
        visited.append(current_vertex)
    for adjacency_vertex in dict1[current_vertex]:
        if adjacency_vertex not in visited:
            stack.append(adjacency_vertex)
outputFile=open('output3.txt','w')
outputFile.writelines(' '.join(map(str,visited)))