#bu kod kullanıcıdan alınan iki stringdeki ortak ve ortak olmayan karakterleri gösterir
x1=str(input(""))
x2=str(input(""))
a1=""
a2=""
a3=""
for i_1 in x1:
    if i_1 in x2:
        a1=a1+i_1
    else:
        a2=a2+i_1
for i_2 in x2:
    if i_2 not in x1:
        a3=a3+i_2
print(a1)
print(a2)
print(a3)
