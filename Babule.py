a=[9, 6, 7, 1, 2]



for j in range(1, len(a)):

    i = j
    while (a[ i - 1 ] > a[ i ])and (i > 0 ):
        t = a[ i - 1 ]
        a[ i - 1 ] = a[ i ]
        a[ i ] = t
        i - = 1

print(a)
