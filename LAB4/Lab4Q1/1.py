#bu kodkullanıcıdan alınan karakter dizinindeki en uzun kelimenin uzunluğunu verir
x=str(input(""))
y=x.split(" ")
a=1
max=a
for j in y:
    if len(j)>max:
        max=len(j)
print(max)
