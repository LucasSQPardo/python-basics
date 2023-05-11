#8 puzzle
#defining movements
move2coord= {'Up':(-1,0), 'Down':(1,0), 'Left':(0,-1), 'Right':(0,1)}
position = lambda mv:move2coord[mv]

def moves(sts):
    new_sts = []
    for st in sts:
        choices = move2coord.keys()
        for c in choices :
            new_sts.append(move(c, st))
    return new_sts

def move(direc, st):
    s,t = st
    newX, newY = addTuple(findZero(s), position(direc))
    if inBound(newX) and inBound(newY):
        val = s[newX][newY]
    else:
        val = 0
    new_s = swap(val,s)
    return (new_s, t + [direc])

def addTuple(current, direction):
    return(current[0] + direction[0], current[1] + direction[1])
    
def inBound(localization):
    if 0 <= localization <= 2 : return True
    return False

def swap (val, s):
    new_s = [si.copy() for si in s]
    x1, y1 = findNum(val, s)
    x2, y2 = findZero(s)
    new_s[x1][y1] = 0
    new_s [x2][y2] = val
    return new_s

def findNum(value, currentMatrix):
    for i, xi in enumerate(currentMatrix):
        for j, xij in enumerate(currentMatrix):
            if(xij == value): return(i,j)

findZero = lambda currentMatrix: findNum(0,currentMatrix)

def AC3(csp, queue):  
    #podemos considerar csp = {X,D,C} onde X são as variáveis, D o domínio das variáveis e C as restrições
	if isEmpty(queue): return True       
    (i,j) = queue.pop()
    revised, csp = Revise(csp, i , j)
    if revised:
    D = csp[1]
    if isEmpty(D[i]): return False
    [queue.push( (k,i) ) for k in neighbors(i,csp) if k!=i]
    return AC3(csp,queue)

def Revise (csp, i, j):
    X, D, C = csp 
    violate = set([violated for violated in D[i] 
        if any( [(x,y) in C[i][j] for D[j] ] )])
    if not empty(violate):
        D[i] -= violate
        return True, (X,D,C)
    return False, csp
