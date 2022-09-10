n=int(input())
def dice(L):
    i=1
    j=0
    L.sort()
    l=len(L)
    while (j<l):
        t=False
        k=0
        
        while (k<len(L)) and (t==False):
            if (i<=L[k]):
                t=True
                L.pop(k)
                i+=1
            else:
                t=False
                k+=1
            
        j+=1
        
    return i-1


for i in range(n):
    y=int(input())
    ch=input().split(" ")
    L=[int(x) for x in ch]
    print("Case #{}:".format(i+1),dice(L))
