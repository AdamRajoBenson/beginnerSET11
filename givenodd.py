o,p=int,input().split()
q=list(map(int,input().split()))
r=[]
for i in q:
    if i%2!=0:
        r.append(i)
print(r[p-1])
