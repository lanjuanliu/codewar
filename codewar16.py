# def odd(n):
#     n=int(input("enter the number"))
#     b=[]
#     i=1
#     while i<n:
#         b.append(i)
#         j=0
#         count=0
#         while j<len(b):
#             if b[j]%2!=0:
#                 count+=1
#             j+=1
#         i+=1
#     return count
# print(odd(n=int(input("enter the num"))))

lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
print(lst)
i=0
count=0
while i<len(lst):
    count+=1
    if lst[i]==count:
        print("none")
    else:
        print(lst[i])
        break
    i+=1