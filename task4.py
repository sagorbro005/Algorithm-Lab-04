inputFile = open('input4.txt', 'r')
f_line = list(map(int, inputFile.readline().split(' ')))
n_vertices, m_edges = f_line[0], f_line[1]
dict1 = {}
# Representing the directed graph with Adjacency List
for i in range(m_edges):
    graph = list(map(int, inputFile.readline().split(' ')))
    ver1, ver2 = graph
    try:
        dict1[ver1].append(ver2)
    except KeyError:
        dict1[ver1] = [ver2]
# DFS Traversal. For finding a cycle in a graph DFS should be used.
visited = [False] * (n_vertices + 1)
stack = [False] * (n_vertices + 1)
check = False
def cycle_finding(dict1, current_vertex=1):
    global check
    visited[current_vertex] = True
    stack[current_vertex] = True
    if current_vertex in dict1:
        for adjacency_vertex in dict1[current_vertex]:
            if stack[adjacency_vertex]:
                check = True
            if not visited[adjacency_vertex]:
                cycle_finding(dict1, adjacency_vertex)
    stack[current_vertex] = False
    return check
# If check is True then the map contains a cycle.Otherwise it doesn't contain any cycle.
if cycle_finding(dict1):    # If check==True
    result='YES'
else:
    result='NO'             # If check!=True
outputFile = open('output4.txt', 'w')
outputFile.writelines(result)
inputFile.close()
outputFile.close()