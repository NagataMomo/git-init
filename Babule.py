a=[9,6,7,1,2]



#for j  in range(len(a)):

i=0
while True:

        if    (a[ i ] < a[i + 1])& (i>=4 ):
        break
    t=a[i]
    a[i]=a[i+1]
    a[i+1]=t
    i+=1

print(a)
