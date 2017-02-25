print("入力：")
line = int(input())
for i in range(line):
    if (i == 0)  :
        total = 0
        a = [total]

    elif (i == 1)  :
        total2 = 1
        a.append(total2)
    else:
        total = a[ i - 1 ] + a[ i - 2 ]
        a.append(total)
print("出力")
print(a)
