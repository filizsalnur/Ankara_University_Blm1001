#bu kod girilen stringin boşluklar göz ardı edildiğinde palindrom olup olmadığını kontrol eder
#palindromsa T, palindron değilse F outputu verir
x=str(input(""))
a=x.split(" ")
b=""
f=True

for i1 in range(len(a)):
    b=b+a[i1]

for i2 in range(len(b)//2):
    if b[i2]!=b[len(b)-1-i2]:
        f=False
if f==True:
    print("T")
elif f==False:
    print("F")
    
