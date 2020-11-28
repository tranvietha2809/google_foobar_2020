def checkIsChildNode2(x, leftNode, rightNode):
    if (x == leftNode or x == rightNode):
        return True
    return False

def findParentNode2(height, x, startingNode):
    rightNode = startingNode - 1
    leftNode = startingNode - 2**(height - 1)
    if(checkIsChildNode2(x, rightNode, leftNode) == True):
        return startingNode
    elif(height> 0):
        if(leftNode <= x <= rightNode):
            height -= 1
            return findParentNode2(height, x , rightNode)
        else:
            height -= 1
            return findParentNode2(height, x, leftNode)

def solution(height, listNum):
    resultArray = [0] * len(listNum)
    for i in range(0, len(listNum)):
        if(listNum[i] == 2** height - 1):
            resultArray[i] = -1
        else:
            parentNode = findParentNode2(height, listNum[i], 2**height - 1)
            print(f"Parent Node of {listNum[i]} is {parentNode}")
            resultArray[i] = parentNode
    return resultArray

solution(3, [7, 3, 5, 1])