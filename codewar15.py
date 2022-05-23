a="lan juan liu"
b=""
c=[]
i=0
while i<len(a):
    if a[i]=="":
        c.append(b)
        b=""
    else:
        b+=a[i]
    i+=1
# if a:
#     b.append(a)
print(b)