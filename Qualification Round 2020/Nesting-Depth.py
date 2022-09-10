n=int(input())
L=[]
def transform(ch):
    cpt=0
    ch1=int(ch[0])*'('
    ch1+=ch[0]
    for i in range (len(ch)-1):
        m=int(ch[i])-int(ch[i+1])
        if m>0:
            ch1+=m*')'
            ch1+=ch[i+1]
        elif m==0:
            ch1+=ch[i+1]
        else:
            ch1+=abs(m)*'('
            ch1+=ch[i+1]
    ch1+=int(ch[-1])*')'
    return ch1
        
for i in range(n):
    ch=input()
    ch1=transform(ch)
    L.append(ch1)
for i in range(n):
    print('Case #%d:'%(i+1),L[i])
