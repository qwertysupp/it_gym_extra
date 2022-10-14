# 1 2 3
# 8 9 4
# 7 6 5
a=int(input())
s=0
def pank(a,s):
    glist=[]
    s=a**0.5
    
    if a%s==0:
        for i in range (int(s)):
            glist.append([])
    else:
        s=s+1
        for i in range (int(s)):
            glist.append([])
    
            
    print(glist)
pank(a,s)
        