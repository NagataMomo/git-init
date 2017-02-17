print("入力：")
line = int(input())
for i in range(line):
    if (i == 0)  :
        total = 0
        list = [total]

    elif (i == 1)  :
        total2 = 1
        list.append(total2)
    else:
        total = list[ i - 1 ] + list[ i - 2 ]
        list.append(total)
print("出力")
print(list)
