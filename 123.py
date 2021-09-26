n=int(input('Dati numarul de elemente din vector='))
a=[]
if n<10:
    print('Introduceti ',n,' elemente pentru vectorul creat')
    for i in range(0,n):
        x=int(input('Dati elementul='))
        a.extend([x])
    print(a)
else:
    print("n este mai mare ca 10")
print('a)  afişează pe ecran componentele tabloului la un interval de 5 poziţii;')
print(a[0:5])
print('b)  afişează pe ecran numerele în ordinea inversă a introducerii în calculator;')
b=[]
b=a
b.reverse()
print(b)
print('c)  sortează componentele tabloului în ordine descrescătoare;')
c=sorted(a)
c.sort(reverse=True)
print(c)
print('d)  afişează pe ecran doar componentele pare;')
f=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        y=a[i]
        f.extend([y])
print(f)
print("e)afişează pe ecran media aritmetică a componentelor pare")
m=[]
l=0
for i in range(0,len(a)):
    if a[i]%2==0:
        l=l+1
        u=a[i]
        m.extend([u])
print(sum(m)//l)
print('f)  afişează pe ecran doar componentele impare;')
r=[]
for i in range(0,len(a)):
    if a[i]%2!=0:
        v=a[i]
        r.extend([v])
print(r)
print('g)  afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt divizibile cu y (valorile x şi y se citesc de la tastatură);')
x=int(input("Introduceti x:"))
y=int(input("Introduceti y:"))
g=[]
for i in range(0,len(a)):
    if (a[i]>x)and(a[i]%y!=0):
        nu=a[i]
        g.extend([nu])
print(g)
print('h)  afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici decât y (valorile x şi y se citesc de la tastatură);')
h=[]
for i in range(0,len(a)):
    if (a[i]>x)and(a[i]<y):
        da=a[i]
        h.extend([da])
print(h)
print('i)  afişează pe ecran poziţiile (indicii) componentelor impare negative;')
print([i for i, e in enumerate(a) if  e & 0 and e<0])
print('j)  afişează pe ecran poziţiile (indicii) componentelor ce conţin doar două cifre semnificative;')
print([i for i, e in enumerate(a) if (e>9 and e<100)or(e<-9 and e>-100)])
print('k)  înlocuieşte prima componentă a tabloului cu componenta de valoare minimă din tabloul respectiv;')
j=a
j[0]=min(j)
print(j)
print("l)înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia;")
l=a.copy()
l[l.index(min(l))]=a[0]
print(l)
print('m)  creează un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatură;')
m=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        kl=a[i]
        m.extend([kl])
print(m)
print('n)  creează un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură;')
n=[]
for i in range(0,len(a)):
    if a[i]%3==0:
        fea=a[i]
        n.extend([fea])
print(n)
print("o)	 creează un tablou nou, format doar din acele componente ale tabloului introdus de la tastatură care au cel mult patru divizori.")
o=[]
for i in a:
    divizori=[]
    for fa in range(1, i+1):
        if i%fa==0:
            divizori.append(fa)
            if fa<0:
                divizori.append(-fa)
    print(divizori)
    if 1<=len(divizori)<=4:
        o.append(i)