n=int(input())
def test(L):
    j=0
    diff =sum(L)-1000000
    if (max(L)>=diff):
        j=L.index(max(L))
        L[j]=L[j]-diff
        return L
    else:
        j=L.index(max(L))
        diff=diff-L[j]
        L[j]=0
        if (max(L)>=diff):
            j=L.index(max(L))
            L[j]=L[j]-diff
            return L
        else:
            j=L.index(max(L))
            diff=diff-L[j]
            L[j]=0
            if (max(L)>=diff):
                j=L.index(max(L))
                L[j]=L[j]-diff
                return L
            else:
                j=L.index(max(L))
                diff=diff-L[j]
                L[j]=0
                
                if (max(L)>= diff):
                    j=L.index(max(L))
                    L[j]=L[j]-diff
                    return L
                else:
                    j=L.index(max(L))
                    diff=diff-L[j]
                    L[j]=0
                    if ( max(L)>= diff):
                        j=L.index(max(L))
                        L[j]=L[j]-diff
                        return L
                    else: return 0


def printer(L1,L2,L3):
    L5=[]
    for i in range(4):
        L5.append(min(L1[i],L2[i],L3[i]))
    if (sum(L5)>=1000000):
        return test(L5)
    else: return "IMPOSSIBLE"
for i in range(n):
    L=[]
    L1=[]
    L2=[]
    Lkol=[]
    for j in range(3):
        w,x,y,z=map(int,input().split())
        Lkol.append(w)
        Lkol.append(x)
        Lkol.append(y)
        Lkol.append(z)
    L=Lkol[0:4]
    L1=Lkol[4:8]
    L2=Lkol[8:12]
    if (printer(L,L1,L2 )=="IMPOSSIBLE"):
        print("Case #{}: IMPOSSIBLE".format(i+1))
    else:
        ch=""
        ch=str(printer(L,L1,L2)[0])+" "+str(printer(L,L1,L2)[1])+" "+str(printer(L,L1,L2)[2])+" "+str(printer(L,L1,L2)[3])
        print("Case #{}:".format(i+1),ch)
        

