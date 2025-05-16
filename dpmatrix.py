arrey=[10,20,50,1,100]
def max_multiple(arrey):
    L=len(arrey)
    T=[[0 for i in range(0,L-1)] for i in range(0,L-1)]
    for p in range(0,L-1):
        for j in range(0,L-1):
            i=j
            if j+p>L-2:
                break
            j=j+p
            swi=0
            for k in range(i,j):
                if swi==0:
                    T[i][j]=T[i][k]+T[k+1][j]+arrey[i]*arrey[k+1]*arrey[j+1]
                    swi=1
                if (T[i][k]+T[k+1][j]+arrey[i]*arrey[k+1]*arrey[j])<T[i][j]:
                    T[i][j]=T[i][k]+T[k+1][j]+arrey[i]*arrey[k+1]*arrey[j+1]
    return T
x=max_multiple(arrey)
print(x[0][len(arrey)-2])