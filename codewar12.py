d=[2,4,7,3,9]
d.sort()
a=[1,2,4,3,5]
i=0
while i<len(a):
    j=0
    while j<len(a)-1:
        if a[j]<a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
        j+=1
    i+=1
print("a",a)
print("d",d)