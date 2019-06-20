n=input()
s=len(n)
l=[]
if(s>=1 and s<=100000):
    for i in range(0,s):
        if(n[i] not in l and n[i]!=" "):
            l.append(n[i])
            d=len(l)
print(d)
