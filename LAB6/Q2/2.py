def ikilik(n):
    global x1
    x1=""
    while n>0:
        x1=str(int(n%2))+x1
        n=int(n/2)

x=int(input(""))
ikilik(x)
print(x1)
