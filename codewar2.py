def find_difference(a, b):
    i=0
    x=1
    while i<len(a):
        x=x*a[i]
        j=0
        y=1
        while j<len(b):
            y=y*b[j]
            if x>y:
                n=x-y
            else:
                n=y-x
            j+=1
        i+=1
    return n
print(find_difference([5,4,4],[3,2,5]))