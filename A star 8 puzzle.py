from copy import deepcopy
def h(oursquare):
    defrents=0
    square=[[1,2,3],[4,5,6],[7,8,0],[0,0]]
    if square==oursquare[:3]:
        oursquare[3][0]=defrents
        return oursquare
    for i in range(0,3):
        for j in range(0,3):
            if square[i][j]!=oursquare[i][j]:
                defrents+=1
    oursquare[3][0]=defrents-1
    return oursquare
def g(oursquare,op):
    swi=0
    for i in range(0,3):
        for j in range(0,3):
            if oursquare[i][j]==0:
                row=i
                column=j
                swi=1
                break
        if swi==1:
            break
    newsquare=deepcopy(oursquare)
    if row!=0 and op=='up':
        newsquare[row][column],newsquare[row-1][column]=newsquare[row-1][column],newsquare[row][column]
        newsquare[3][1]+=1
        newsquare[3].append('up')
    elif op=='up':
        newsquare=None
    if row!=2 and op=='down':
        newsquare[row][column],newsquare[row+1][column]=newsquare[row+1][column],newsquare[row][column]
        newsquare[3][1]+=1
        newsquare[3].append('down')
    elif op=='down':
        newsquare=None
    if column!=2 and op=='right':
        newsquare[row][column],newsquare[row][column+1]=newsquare[row][column+1],newsquare[row][column]
        newsquare[3][1]+=1
        newsquare[3].append('right')
    elif op=='right':
        newsquare=None
    if column!=0 and op=='left':
        newsquare[row][column],newsquare[row][column-1]=newsquare[row][column-1],newsquare[row][column]
        newsquare[3][1]+=1
        newsquare[3].append('left')
    elif op=='left':
        newsquare=None
    return newsquare
def select(oursquare):
    square=[[1,2,3],[4,5,6],[7,8,0]]
    if square==oursquare[:3]:
        return oursquare
    x=[]
    x.append(g(oursquare,'up'))
    x.append(g(oursquare,'down'))
    x.append(g(oursquare,'right'))
    x.append(g(oursquare,'left'))
    x=[n for n in x if n!=None]
    while True :
        y=[]
        for i in x:
            y.append(i[3][0]+i[3][0])
        c=min(y)
        ind=y.index(c)
        temp=x.pop(ind)
        for i in x:
            t=i[:3]
            if square==t:
                print(i[3][2:])
                return
        x.append(g(temp,'up'))
        x.append(g(temp,'down'))
        x.append(g(temp,'right'))
        x.append(g(temp,'left'))
        x=[n for n in x if n!=None]
oursquare=[[1,3,6],[5,0,2],[4,7,8],[0,0]]
select(oursquare)