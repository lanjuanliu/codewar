a=[2,2,3]
b=[5,4,1]
i=0
x=1
while i<len(a):
    x=x*a[i]
    j=0
    y=1
    while j<len(b):
        y=y*b[j]
        j+=1
    i+=1
print("volumes of a",x)
print("volume of b",y)
