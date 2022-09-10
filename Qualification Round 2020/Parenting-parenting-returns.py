n=int(input())
L2=[]
def tache(L,t):
    ch1=''
    ch='C'
    C=[]
    C.append(L[0])
    C.append(L[1])
    J=[]
    for i in range(2,len(L)-1,2):
        T=True
        T1=True
        c=0
        while (c<len(C)-1) and (T==True):
            if (((int(L[i])>= int(C[c])))and((int(L[i])< int(C[c+1]))))or(((int(L[i+1])>int(C[c])))and((int(L[i+1])<= int(C[c+1])))):
                T=False
                
            else:c+=2
                
        if T==True:
            C.append(L[i])
            C.append(L[i+1])
            ch+='C'
        else:
            if len(J)==0:
                J.append(L[i])
                J.append(L[i+1])
                ch+='J'
            else:
                j=0
                while(j<len(J)-1)and (T1==True):
                    if (((int(L[i])>= int(J[j])))and((int(L[i])< int(J[j+1]))))or(((int(L[i+1])> int(J[j])))and((int(L[i+1])<= int(J[j+1])))):
                        T1=False
                    else:j+=2
                        
                if T1==True:
                    J.append(L[i])
                    J.append(L[i+1])
                    ch+='J'
                    
                else:ch1='IMPOSSIBLE'
    

    if ch1=='IMPOSSIBLE':
        return ch1
    else: return ch
    


    

for i in range(n):
    t=int(input())
    L=[]
    for k in range(t):
        L+=input().split(' ')
    ch=tache(L,t)
    L2.append(ch)
    
for j in range(len(L2)):
    print('Case #%d:'%(j+1),L2[j])

