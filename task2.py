inputFile=open('input2.txt','r')
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
outputFile=open('output2.txt','w')
# for key in sorted(dict1.keys()):
#     values=sorted(dict1[key])
#     outputFile.writelines(f'{key} : {values}\n')

# BFS Traversal
visited=[1]     # Our traversal always starts from vertex 1
queue=[1]
while queue:
    current_vertex=queue.pop(0)
    for adjacency_vertex in dict1[current_vertex]:
        if adjacency_vertex not in visited:
            visited.append(adjacency_vertex)
            queue.append(adjacency_vertex)
outputFile.writelines(' '.join(map(str,visited)))
inputFile.close()
outputFile.close()