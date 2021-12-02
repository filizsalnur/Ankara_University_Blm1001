f1=[]
f2=[]
f3=[]
y1=[]
y2=[]
y3=[]


def not_al():
    x1=int(input(""))
    x2=int(input(""))
    x3=int(input(""))
    f1.append(x1)
    f2.append(x2)
    f3.append(x3)
    return x1 and x2 and x3

def ortalama_hesapla(a,b,c):
    z1=a/count
    z2=b/count
    z3=c/count
    y1.append(z1)
    y2.append(z2)
    y3.append(z3)
    return z1 and z2 and z3

def ortalama_bas():
    print(count)
    print(y1[0])
    print(y2[0])
    print(y3[0])
    
a=0
b=0
c=0
count=1
not_al()
a=a+float(f1[0])
b=b+float(f2[0])
c=c+float(f3[0])
flag=input("")
while flag!="end":
    not_al()
    a=a+float(f1[count])
    b=b+float(f2[count])
    c=c+float(f3[count])
    count=count+1
    flag=input("")
    
ortalama_hesapla(a,b,c)
ortalama_bas()

    
