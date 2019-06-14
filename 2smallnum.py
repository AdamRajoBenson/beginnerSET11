p,q=int,input().split()
r=0
s=[]
o=input().split()
for i in o:
  s.append(i)
s.sort()
print(s[q-1])
