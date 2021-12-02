a=(int(input("Kenar1: ")))
b=(int(input("Kenar2: ")))
c=(int(input("Kenar3: ")))
if a==b and b==c:
    print("eskenar ucgen")
elif a==b and a!=c or a==c and a!=b or b==c and a!=b:
    print("ikizkenar ucgen")
else:
    print("cesitkenar ucgen")



