
n=int(input("Dati numarul de elemente din vector:"))
a=[]
if n < 10 and n>0:
    print('Introduceti',n,'elemente:')
for i in range(0, n):
        n1=int(input("Dati elementul:"))
        a.extend([n1])
ee=a.copy()
print(",".join(map(str, a)))
print('a)  afişează pe ecran componentele tabloului la un interval de 5 poziţii:')
b=a[::5]
print(b)
print('b)  afişează pe ecran numerele în ordinea inversă a introducerii în calculator:')
c=a[::-1]
print(c)
print('c)  sortează componentele tabloului în ordine descrescătoare:')
d=sorted(a)
d.sort(reverse=True)
print(d)
print("d)afişează pe ecran doar componentele pare")
e=[]
for f in range(0, len(a)):
    if a[f]%2==0:
        g=a[f]
        e.extend([g])
print(e)
print("e)afişează pe ecran media aritmetică a componentelor pare")
if len(e)>0:
    print(sum(e)/len(e))
print('f)  afişează pe ecran doar componentele impare:')
g=[]
for i in range(0,len(a)):
    if a[i]%2!=0:
        h=a[i]
        g.extend([h])
print(g)
print('g)  afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt divizibile cu y:')
x=int(input("Dati un numar:"))
y=int(input("Dati un numar:"))
j=[]
for i in range(0,len(a)):
    if a[i]%y!=0 and a[i]>x:
        k=a[i]
        j.extend([k])
print(j)
print('h)afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici decât y :')
x=int(input("Dati un numar:"))
y=int(input("Dati un numar:"))
l=[]
for i in range(0,len(a)):
    if a[i]<y and a[i]>x:
        bb=a[i]
        l.extend([bb])
print(l)
print('i)  afişează pe ecran poziţiile (indicii) componentelor impare negative:')
p=[]
for i in range(0,len(a)):
    if (a[i]%2!=0 and a[i]<0):
        p.append(i)
print(p)
print('j)  afişează pe ecran poziţiile (indicii) componentelor ce conţin doar două cifre semnificative;')
q=[]
for i in range(0,len(a)):
    if (a[i]>9 and a[i]<100)or(a[i]<-9 and a[i]>-100):
        q.append(i)
print(a)
print('k)  înlocuieşte prima componentă a tabloului cu componenta de valoare minimă din tabloul respectiv:')
u=a.copy()
u[0]=min(u)
print(u)
print('l)  înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia:')
aa=a.copy()
s=min(aa)
aa[aa.index(s)]=aa[0]
print(aa)
print('m)  creează un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatură;')
bb=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        y=a[i]
        bb.extend([y])
print(bb)
print('n)  creează un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură:')
cc=[]
for i in range(0,len(a)):
    if a[i]%3==0:
        y=a[i]
        cc.extend([y])
dd=cc
print(dd)
print('o)  creează un tablou nou, format doar din acele componente ale tabloului in-trodus de la tastatură care au cel mult patru divizori:')
ee=[]
for i in a:
    if i>0:
        ff=0
        for x in range(1,i+1):
            if i%x==0:
                ff+=1
        if ff<=4:
            ee.append(i)
print(ee)