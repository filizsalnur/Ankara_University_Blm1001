a="Ejderha"
b="Yilan"
c="At"
d="Koyun"
e="Maymun"
f="Horoz"
g="Kopek"
h="Domuz"
i="Fare"
j="Okuz"
k="Kaplan"
l="Tavsan"
x=int(input("Yil: "))
if x%12==8:
    print(x,":", a)
elif x%12==9:
    print(x,":", b)
elif x%12==10:
    print(x,":", c)
elif x%12==11:
    print(x,":", d)
elif x%12==0:
    print(x,":", e)
elif x%12==1:
    print(x,":", f)
elif x%12==2:
    print(x,":", g)
elif x%12==3:
    print(x,":", h)
elif x%12==4:
    print(x,":", i)
elif x%12==5:
    print(x,":", j)
elif x%12==6:
    print(x,":", k)
else:
    print(x,":", l)
