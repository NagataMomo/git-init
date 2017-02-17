a=[9,6,7,1,2]

for i in range(4):#01234
   if  a[ i ] < a[i + 1]:
       t=a[i]
       a[i]=a[i+1]
       a[i+1]=t


print(a)
