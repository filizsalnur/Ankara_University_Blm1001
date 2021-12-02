def ort(a):
    global zq
    son=0
    for i in range(len(a)):
        son=son+float(a[i])
    b=son/len(a)+0.005
    zq=("%5.2f"%b+"\t")
    
    

    

    
def yaso(a):
    global q
    if int(a[2])+1<10:
        q=(a[0]+"-"+a[1]+"-"+str(0)+str(int(a[2])+1))
    else:
        q=(a[0]+"-"+a[1]+"-"+str(int(a[2])+1))

def fis2(a,b,d):
    global c2
    c2=[]
    a1=0
    while a1<=31:
        if a1==int(b[2])+1 and int(a[1])+d==int(b[1]) :
            break
        elif int(a[1])+d==int(a[1]) and a1<int(a[2]):
            a1=a1+1
        else:
            if a1<10:
                if int(a[1])+d<10:
                    c2.append(a[0]+"-"+str(0)+str(int(a[1])+d)+"-"+str(0)+str(a1))
                    a1=a1+1
                else:
                    c2.append(a[0]+"-"+str(int(a[1])+d)+"-"+str(0)+str(a1))
                    a1=a1+1
            else:
                if int(a[1])+d<10:
                    c2.append(a[0]+"-"+str(0)+str(int(a[1])+d)+"-"+str(a1))
                    a1=a1+1
                else:
                    c2.append(a[0]+"-"+str(int(a[1])+d)+"-"+str(a1))
                    a1=a1+1




def fis(a,b):
    global c1
    c1=[]
    a2=0
    while a2<=(int(b[1])-int(a[1])):
        a1=1
        if int(a[1])+a2==int(b[1]):
            while a1<=int(b[2]):
                if a1==int(b[2])+1 and int(a[1])+a2==int(b[1]) :
                    break
                elif int(a[1])+a2==int(a[1]) and a1<int(a[2]):
                    a1=a1+1
                else:
                    if a1<10:
                        if int(a[1])+a2<10:
                            c1.append(a[0]+"-"+str(0)+str(int(a[1])+a2)+"-"+str(0)+str(a1))
                            a1=a1+1
                        else:
                            c1.append(a[0]+"-"+str(int(a[1])+a2)+"-"+str(0)+str(a1))
                            a1=a1+1
                    else:
                        if int(a[1])+a2<10:
                            c1.append(a[0]+"-"+str(0)+str(int(a[1])+a2)+"-"+str(a1))
                            a1=a1+1
                        else:
                            c1.append(a[0]+"-"+str(int(a[1])+a2)+"-"+str(a1))
                            a1=a1+1
        else:
            while a1<=31:
                if a1==int(b[2])+1 and int(a[1])+a2==int(b[1]):
                    break
                elif int(a[1])+a2==int(a[1]) and a1<int(a[2]):
                    a1=a1+1
                else:
                    if a1<10:
                        if int(a[1])+a2<10:
                            c1.append(a[0]+"-"+str(0)+str(int(a[1])+a2)+"-"+str(0)+str(a1))
                            a1=a1+1
                        else:
                            c1.append(a[0]+"-"+str(int(a[1])+a2)+"-"+str(0)+str(a1))
                            a1=a1+1
                    else:
                        if int(a[1])+a2<10:
                            c1.append(a[0]+"-"+str(0)+str(int(a[1])+a2)+"-"+str(a1))
                            a1=a1+1
                        else:
                            c1.append(a[0]+"-"+str(int(a[1])+a2)+"-"+str(a1))
                            a1=a1+1
        a2=a2+1
                
dosya=open("covid_data.txt","r")
x=input("")
y1=input("")
y2=input("")
a1=y1.split("-")
a2=y2.split("-")
fis(a1,a2)
yaso(a2)

    
z8=int(a2[1])-int(a1[1])+1

s=""
fi3=[]
fi4=[]
fi5=[]

while True:
    z=dosya.readline()
    d=z.split("\t")
    if x in z:
        for i in range(len(c1)+1):
            if i<len(c1) and c1[i] in z:
                fi3.append(int(d[3]))
                fi4.append(int(d[4]))
                fi5.append(int(d[5]))
    else:
        if d[1]!="Country/Region":
            if str(d[1])>str(x):
                dosya.close()
                break
ort(fi3)
s=s+zq
ort(fi4)
s=s+zq
ort(fi5)
s=s+zq
s=s+"\n"    



for i1 in range(z8):
    f3=[]
    f4=[]
    f5=[]
    fis2(a1,a2,i1)
    dosya=open("covid_data.txt","r")
    while True:
        z=dosya.readline()
        d=z.split("\t")
        if x in z:
            for i in range(len(c2)+1):
                if i<len(c2) and c2[i] in z:
                    f3.append(int(d[3]))
                    f4.append(int(d[4]))
                    f5.append(int(d[5]))
        else:
            if d[1]!="Country/Region":
                if str(d[1])>str(x):
                    dosya.close()
                    break

    ort(f3)
    s=s+zq
    ort(f4)
    s=s+zq
    ort(f5)
    s=s+zq
    s=s+"\n"

zw=x+".txt"
xi=open(zw,"w")
xi.write(s)
xi.close()
         
    






