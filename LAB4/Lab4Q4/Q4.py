#input'u ters çevirip Büyük harfleri ve boşlukları korur
x=input("")
a=""
i=len(x)-1
while i>=0:
    if not x[i]==" ":
        a=a+x[i]
    i=i-1
a=a.lower()
p=0
z=0
a2=""
while p<len(x):
    if x[p]==" ":
        a2=a2+" "
    elif 65<=ord(x[p])<=90:
        a2=a2+a[z].upper()
        z=z+1
    else:
        a2=a2+a[z]
        z=z+1
    p=p+1
print(a2)









