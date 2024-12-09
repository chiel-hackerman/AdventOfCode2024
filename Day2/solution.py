from itertools import count

file = open('input.txt')

results = []

def checkList(x):
    r = len(x)-1
    diff=[]
    for m in range(r):
        diff.append(x[m]-x[m+1])

    pos = sum(1 for i in diff if i < 0)
    neg = sum(1 for i in diff if i > 0)
    l = len(diff)
    # Step larger than three or the same
    if any(y>3 for y in diff) or any(y < -3 for y in diff) or any(y==0 for y in diff):
        return False
    elif pos == l or neg == l:
        return True
    else:
        return False

def checkLoop(x):
    resultsLoop = []
    for y in range(len(x)):
        xnew = x.copy()
        del xnew[y]
        resloop = checkList(xnew)
        resultsLoop.append(resloop)
    if any(resultsLoop):
        return True
    else:
        return False

while True:
    content=file.readline()
    if not content:
        break
    x = content.split()
    
    list = []
    for n in x:
        list.append(int(n))
    
    result = checkList(list)
    
    if result == False:
        result = checkLoop(list)
    
    results.append(result)

print(results.count(True))