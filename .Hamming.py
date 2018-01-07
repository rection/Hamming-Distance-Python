
#!/bin/python
#Calistirmak icin:  mpiexec -n 4 python olsa.py

from random import randint


sum=0
a = []
b = []
z = randint(0,10000)
for rast in range(0,z):
                k = randint(0,1)
                l = randint(0,1)
                a.append(k)
                b.append(l)


p = 0
for pos in range(0,z):
                if a[pos] != b[pos]:
                        print  pos ,'degerinde esit degildir a degeri ' ,a[pos] ,'b degeri' ,b[pos]
                        p += 1

print 'Hamming mesafesi ' , p


