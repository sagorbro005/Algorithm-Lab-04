inputFile = open('input1b.txt','r')
f_line = list(map(int,inputFile.readline().split(' ')))
n_vertices,m_edges = f_line[0],f_line[1]
list1 = [0]*(n_vertices+1)
for i in range(n_vertices+1):
    list1[i] = []
for j in range(m_edges):
    graph = list(map(int,inputFile.readline().split(' ')))
    ver1, ver2, weight=graph
    list1[ver1].append((ver2, weight))
outputFile=open('output1b.txt','w')
for k in range(n_vertices+1):
    x = ' '.join(map(str, list1[k]))
    outputFile.writelines(f'{k} : {x}\n')
inputFile.close()
outputFile.close()