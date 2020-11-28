def solution(total_lambs):
    return leastGen(total_lambs) - mostGen(total_lambs)
    
def mostGen(x):
    startArr = [1 ,2]
    if(x == 1 or x == 2):
        return 1
    while(True):
        nextNum = startArr[-1] * 2
        if(x< nextNum + sum(startArr)):
            break
        startArr.append(nextNum)
    return(len(startArr))

def leastGen(x):
    startArr = [1 ,1]
    if(x == 1):
        return 1
    if(x == 2 or x == 3):
        return 2
    while(True):
        nextNum = startArr[-1] + startArr[-2]
        if(x < nextNum + sum(startArr)):
            break
        startArr.append(nextNum)
    return(len(startArr))
