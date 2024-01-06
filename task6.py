inputFile = open("input6.txt", 'r')
row,col = list(map(int,inputFile.readline().split(' ')))
# Initializing 2D matrix filled with zeros
matrix=[0]*row
for i in range(row):
    matrix[i]=[0]*col
# Converting the given graph into a list
graph=inputFile.read().strip().split('\n')
# Filled the matrix with the given data of the graph
for i in range(row):
    for j in range(col):
        matrix[i][j]=graph[i][j]
# Initializing another 2D matrix named visited filled with False
visited=[0]*row
for i in range(row):
    visited[i]=[False]*col
# The checker function checks if a given cell (i, j) is valid or not.
# It returns False if the cell is out of bounds, already visited, or blocked (matrix[i][j]=="#").
# Otherwise, it marks the cell as visited and returns True.
def checker(matrix, i, j):
    global visited
    global row
    global col

    if i<0:
        return False
    if i>=row:
        return False
    if j<0:
        return False
    if j>=col:
        return False
    if visited[i][j]:
        return False
    if matrix[i][j]=="#":
        return False
    if matrix[i][j]=="." or matrix[i][j]=="D":
        visited[i][j] = True
        return True
# The finding_dmd function performs DFS from a given cell (x, y).
# It returns 0 if the cell is not valid.
# Otherwise, it recursively performs from all four neighboring cells and returns the total number of cells marked "D".
def finding_dmd(matrix, x, y):
    if not checker(matrix, x, y):
        return 0
    else:
        count_dmd = 0
        if matrix[x][y]=="D":
            count_dmd += 1
        count_dmd += finding_dmd(matrix, x-1, y)    # left neighbour
        count_dmd += finding_dmd(matrix, x+1, y)    # right neighbour
        count_dmd += finding_dmd(matrix, x, y+1)    # up neighbour
        count_dmd += finding_dmd(matrix, x, y-1)    # down neighbour

    return count_dmd
# The next block of code performs from each cell in matrix that is marked "." and not yet visited,
# and keeps track of the maximum number of cells marked "D" found during traversal.
max_count_dmd = 0
for i in range(row):
    for j in range(col):
        if matrix[i][j] == '.' and not visited[i][j]:
            count_dmd = finding_dmd(matrix, i, j)
            max_count_dmd = max(max_count_dmd, count_dmd)
outputFile=open('output6.txt','w')
outputFile.writelines(str(max_count_dmd))
inputFile.close()
outputFile.close()