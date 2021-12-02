c=-1
b=int(input(""))
a=b+2
while True:
    a=a-1
    c=c+1
    if c==1:
        print(a*"*")
    elif c>1:
        print((c-2)*" ",a*"*")
    
    if a==0:
        break
