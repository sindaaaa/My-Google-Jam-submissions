n=int(input())
def punched(r,c):
    out=".."+(c-1)*"+-"+"+\n"
    out+=".."+(c-1)*"|."+"|\n"
    out+=c*"+-"+"+"
    for i in range (r-1):
        out+="\n|"+c*".|"
        out+="\n+"+c*"-+"
    return out
for j in range(n):
    r,c=map(int,input().split(" "))
    print("Case #{}:".format(j+1))
    print(punched(r,c))
