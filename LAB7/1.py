harf_a=input("")
a=[]
c1=1
while c1<11:
    x=int(input(""))
    a.append(x)
    c1=c1+1

harf_b=input("")
b=[]
c2=1
while c2<11:
    x=int(input(""))
    b.append(x)
    c2=c2+1

aa=[]
bb=[]
for i in range(26):
    aa.append(harf_a[i])
    bb.append(harf_b[i])


aa_1=[]
bb_1=[]

for i1 in range(10):
    aa_1.append(int(b[i1]))
    bb_1.append(int(a[i1]))


aa_2=[]
bb_2=[]
for i2 in range(26):
    if i2 not in aa_1:
        aa_2.append(aa[i2])
    if i2 not in bb_1:
        bb_2.append(bb[i2]) 


son_a=0
son_b=0

for f in range(16):
    f_a=ord(aa_2[f])
    f_b=ord(bb_2[f])
    if f_a<f_b:
        son_b=son_b+f_b-f_a
    elif f_a>f_b:
        son_a=son_a+f_a-f_b
    
z={}
z['A']=son_a
z['B']=son_b
print(z)



    
    
