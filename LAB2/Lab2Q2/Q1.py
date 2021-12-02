x=int(input())
z=10000000000000000000000000
min=z
for number in range(x):
    b=int(input())
    if b<z:
        min=b
        z=b
print(min)
