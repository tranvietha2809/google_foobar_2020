from collections import deque

def findShortestPath(array):
    colNum = len(array[0])
    rowNum = len(array)
    visited = [[False for x in range(colNum)] for y in range(rowNum)]
    row = [-1, 0, 0, 1]
    col = [0, -1, 1, 0]
    min_dist = 1000*1000*1000
    destX = rowNum - 1
    destY = colNum -1

    visited[0][0] = True

    possibleNodes = deque()
    possibleNodes.append((0, 0, 1))

    while possibleNodes:
        (currentX, currentY, distTravelled) = possibleNodes.popleft()
        if(currentX == destX and currentY == destY):
            min_dist = distTravelled
            break
        for k in range(4):
            rrow = currentX + row[k]
            rcol = currentY + col[k]
            if isValid(array, visited, rrow, rcol):
                visited[rrow][rcol] = True
                possibleNodes.append((rrow,rcol, distTravelled + 1))
    return min_dist
def isValid(array, visited, currentX, currentY):
    colNum = len(array[0])
    rowNum = len(array)
    return (currentX >= 0) and (currentX < rowNum) and (currentY >= 0) and (currentY < colNum) and array[currentX][currentY] == 0 and not visited[currentX][currentY]



def solution(array):
    min_dist1 = findShortestPath(array);
    colNum = len(array[0])
    rowNum = len(array)
    onesLocations = deque()

    for i in range(rowNum):
        for k in range(colNum):
            if array[i][k] == 1:
                onesLocations.append((i, k))
    while onesLocations:
        array1 = array
        (m, n) = onesLocations.popleft()
        array1[m][n] = 0
        min_dist2 = findShortestPath(array1)
        min_dist1 = min(min_dist1, min_dist2)
        array1[m][n] = 1
    return min_dist1