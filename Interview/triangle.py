def getArea(x,y):

    def getBase(base, height):
        index = []
        h = 0
        for i in range(len(base)):
            if base[i] == 0:
                index.append(i)
            else:
                h = i
        
        base = abs(height[index[0]]-height[index[1]])
        return (base, h)



    if x.count(0) == 2:
        base, height = getBase(x,y)
    else:
        base, height = getBase(y,x)

    return base*height/2


def getArea(x,y):

    def getBase(base, height):
        b = 0
        h = 0
        for i in range(len(base)):
            if base[i] == 0:
                b = abs(b-height[i])
            else:
                h = i
        
        return (b, h)



    if x.count(0) == 2:
        base, height = getBase(x,y)
    else:
        base, height = getBase(y,x)

    return base*height/2