import sys



movments = {
    ( -2,1) : "UR",
    (0 , 2) : "R",
    ( 2,1)  : "LR",
    ( -2,-1): "UL",
    (0, -2) : "L",
    (2,-1) : "LL",
    "UR" : (-2, 1) ,
    "LL" : (2, -1) ,
    "LR" : (2, 1) ,
    "UL" : (-2, -1) ,
    "L" : (0, -2) ,
    "R" : (0, 2)
}

def printShortestPath(n, i_start, j_start, i_end, j_end):
    print "i_start, j_start, i_end, j_end", i_start, j_start, i_end, j_end
    di, dj = i_end - i_start, j_end - j_start
    print di, dj
    if isAvailable(di, dj) == False:
        print "Impossible"
        return "Impossible"
    path = []
    while di != 0 or dj != 0:
        if di == 0:
            if dj > 0:
                count = dj // 2
                path += ["R"] * count
                di -= count * movments["R"][0]
                dj -= count * movments["R"][1]
            else:
                count = dj // -2
                path += ["L"] * count
                di -= count * movments["L"][0]
                dj -= count * movments["L"][1]
        elif dj == 0:
            if di < 0:
                count = di // -4
                path += ["UL", "UR"] * count
                di -= count * movments["UL"][0]
                dj -= count * movments["UL"][1]
                di -= count * movments["UR"][0]
                dj -= count * movments["UR"][1]
            else:
                count = di // 4
                path += ["LL", "LR"] * count
                di -= count * movments["LL"][0]
                dj -= count * movments["LL"][1]
                di -= count * movments["LR"][0]
                dj -= count * movments["LR"][1]
        else: break
        print path, di, dj
    print str(len(path))
    print " ".join(sortInOrder(path))
    return str(len(path)) +"\n"+" ".join(sortInOrder(path))

def isAvailable(di,dj):
    di = abs(di)
    dj = abs(dj)

    if di % 2 == 1: return False
    elif di % 4 == 0 and dj % 2 == 1: return False
    elif di % 4 == 2 and dj % 2 == 0: return False
    else: return True

def sortInOrder(path):
    priority = ['UL', 'UR', 'R', 'LR', 'LL', 'L']
    sortedInOrder = []
    for item in priority:
        if item in path:
            sortedInOrder += [item] * path.count(item)
    return sortedInOrder
if __name__ == "__main__":
    printShortestPath(9,8,4,0,4)

    # n = int(raw_input().strip())
    # i_start, j_start, i_end, j_end = raw_input().strip().split(' ')
    # i_start, j_start, i_end, j_end = [int(i_start), int(j_start), int(i_end), int(j_end)]
    # printShortestPath(n, i_start, j_start, i_end, j_end)


