inputFile = open('input5.txt', 'r')
f_line = list(map(int, inputFile.readline().split(' ')))
n_vertices, m_edges, target = f_line[0], f_line[1], f_line[2]
dict1 = {}

# Representing the undirected graph with Adjacency List
for i in range(m_edges):
    graph = list(map(int, inputFile.readline().split(' ')))
    ver1, ver2 = graph
    try:
        dict1[ver1].append(ver2)
    except KeyError:
        dict1[ver1] = [ver2]
    try:
        dict1[ver2].append(ver1)
    except KeyError:
        dict1[ver2] = [ver1]

# BFS Traversal. For unweighted and undirected graph BFS should be used.
visited = [False] * (n_vertices + 1)
queue = [1]        # Our traversal always starts from vertex 1
parent = [0] * (n_vertices + 1)
visited[1] = True
while queue:
    current_vertex = queue.pop(0)       # First In First Out
    for adjacency_vertex in dict1[current_vertex]:
        if not visited[adjacency_vertex]:
            visited[adjacency_vertex] = True
            queue.append(adjacency_vertex)
            parent[adjacency_vertex] = current_vertex
# Reconstruct the shortest path
short_path = []
while target != 0:
    short_path.append(target)
    target = parent[target]
short_path = short_path[::-1]   # reverse the shortest path
outputFile = open('output5.txt', 'w')
path=' '.join(map(str,short_path))
# Time will be the number of edges for the shortest path
outputFile.writelines(f'Time: {str(len(short_path)-1)}\nShortest Path: {path}')
inputFile.close()
outputFile.close()