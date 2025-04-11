def locate(loc):
    x = loc[0]
    y = int(loc[1])-1
    if x=='a':
        x=0
    elif x=='b':
        x=1
    elif x=='c':
        x=2
    elif x=='d':
        x=3
    elif x=='e':
        x=4
    elif x=='f':
        x=5
    elif x=='g':
        x=6
    elif x=='h':
        x=7
    else:
        return "Invalid",""
    if y > 7 or y < 0:
        return "Invalid",""
    return x,y


def diagonal(v1,v2):
    x1, y1 = locate(v1)
    x2, y2 = locate(v2)

    if x1 == "Invalid" or x2 == "Invalid":
        return False

    list=[]
    for i in range(8):
        list +=[[x1+i,y1+i],[x1+i,y1-i],[x1-i,y1-i],[x1-i,y1+i]]
    if [x2,y2] in list:
        return True
    else:
        return False


def orthogonal(v1,v2):
    x1, y1 = locate(v1)
    x2, y2 = locate(v2)
    
    if x1 == "Invalid" or x2 == "Invalid":
        return False

    list=[]
    for i in range(8):
        list +=[[x1,y1+i],[x1,y1-i],[x1-i,y1],[x1+i,y1]]
    if [x2,y2] in list:
        return True
    else:
        return False


def legal(piece,v1,v2)
    x1, y1 = locate(v1)
    x2, y2 = locate(v2)

    if piece == K:
        if orthogonal(v1,v2) == True or diagonal(v1,v2) == True:
            return True
        else:
            return False
    if piece == R:
        if orthogonal(v1,v2) == True:
            return True
        else:
            return False
    if piece == B:
        if diagonal(v1,v2) == True:
            return True
        else:
            return False
    if piece == P:
        if [x2,y2] == [x1,y1+1]:
            return True
        else:
            return False
    if piece == N:
        if [x2,y2] == [x1+2,y1+1] or [x2,y2] == [x1+2,y1-1] or [x2,y2] == [x1-2,y1+1] or [x2,y2] == [x1-2,y1-1] or [x2,y2] == [x1+1,y1+2] or [x2,y2] == [x1-1,y1+2] or [x2,y2] == [x1+1,y1-2] or [x2,y2] == [x1-1,y1-2]:
            return True
        else:
            return False
    if piece == Q:
        if [x2,y2] == [x1+1,y1] or [x2,y2] == [x1+1,y1+1] or [x2,y2] == [x1+1,y1-1] or [x2,y2] == [x1,y+1] or [x2,y2] == [x1,y1-1] or [x2,y2] == [x1-1,y1] or [x2,y2] == [x1-1,y1+1] or [x2,y2] == [x1-1,y1-1]:
            return True
        else:
            return False
    