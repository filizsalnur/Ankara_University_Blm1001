#kelimelerin bas harflerini yazar
def bosluk(n):
    x1=""
    y=n
    y1=y.split(" ")
    for i in y1:
        x1=x1+i[0]
    print(x1)    
x=input("")
bosluk(x)


    
