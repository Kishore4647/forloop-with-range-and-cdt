l=[11,22,33,44,55,66]
for ip in range(0,len(l),2):
    l[ip],l[ip+1]=l[ip+1],l[ip]
print(l)