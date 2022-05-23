def lst(a):
    i=0
    x=[]
    while i<len(a):
        d=a[i]*a[i]
        x.append(d)
        i+=1
    return x
print(lst([2,3,4]))
