a=[3,7,8]
b=[]
i=0
while i<len(a):
    j=a[i]
    while j<=a[-1]:
        b.append(j)
        j+=1
        i+=1
print(b)
