def cross(arrey,low,high):
    if low==high:
        return arrey[low]
    mid=(low+high)//2
    lsum=cross(arrey,low,mid)
    rsum=cross(arrey,mid+1,high)
    suml=float('-inf')
    temp=0
    for i in range(mid,low-1,-1):
        temp+=arrey[i]
        suml=max(suml,temp)
    sumr=float('-inf')
    temp=0
    for i in range(mid+1,high+1):
        temp+=arrey[i]
        sumr=max(sumr,temp)
    csum=suml+sumr
    return max(lsum,rsum,csum)
l=[13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
print(cross(l,0,len(l)-1))