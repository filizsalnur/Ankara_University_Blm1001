x=int(input(""))
f=0
d=0
while f<x:
    f=f+1
    if f%2!=0:
        d=d+4/(2*f-1)
    elif f%2==0:
        d=d-4/(2*f-1)
print(d)
