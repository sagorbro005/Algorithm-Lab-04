inputFile=open('input1a.txt','r')
n_vertices,m_edges=list(map(int,inputFile.readline().split(' ')))
# n_vertices,m_edges=f_line[0],f_line[1]
matrix=[0]*(n_vertices+1)
for i in range(n_vertices+1):
    matrix[i]=[0]*(n_vertices+1)
for j in range(m_edges):
    graph=list(map(int,inputFile.readline().split(' ')))
    row,col,weight=graph
    matrix[row][col]=weight
outputFile=open('output1a.txt','w')
for k in range(n_vertices+1):
    outputFile.writelines(' '.join(map(str,matrix[k]))+'\n')
inputFile.close()
outputFile.close()
