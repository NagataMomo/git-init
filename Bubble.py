a=[9, 6, 7, 1, 2]



for i in range(1, len(a)):

    j = i
    while (a[ j - 1 ] > a[ j ])and (j > 0 ):
        t = a[ j - 1 ]
        a[ j - 1 ] = a[ j ]
        a[ j ] = t #a[j], a[j - 1] = a[j - 1], a[j]でもOK
        #j - = 1
        j = j - 1

print(a)
