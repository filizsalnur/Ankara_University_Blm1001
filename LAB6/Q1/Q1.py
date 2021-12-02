
fiyat=input("")
liste1=fiyat.split(" ")
adet=input("")
liste2=adet.split(" ")

def tutar(n1,n2):
    global tutar
    a=0
    tutar=0
    while a<len(n1):
        tutar=tutar+int(n1[a])*int(n2[a])
        a=a+1


def indirim(n):
    global x1,a
    if n<100:
        x1=(n*10/100)
        a=10
    elif n<500 and n>100:
        x1=(n*15/100)
        a=15
    else:
        x1=(n*20/100)
        a=20

def son_tutar(n1,n2):
    global x2
    x2=n1-n2


tutar(liste1,liste2)
indirim(tutar)
son_tutar(tutar,x1)
print(tutar,end=" ")
print(a,end=" ")
print(x2,end=" ")



    
    
    
    
