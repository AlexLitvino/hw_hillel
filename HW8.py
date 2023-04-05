import sys

min_width = int(input("Enter minimal width:"))
max_width = int(input("Enter maximal width:"))

if min_width > max_width:
    print("minimal width more than maximal width")
    sys.exit()

if (max_width - min_width) % 2 != 0:
    print("Number not a multiple of 2")
    sys.exit()

for k in range(1, max_width + 1):                #формирую столбцы для первой половины кристалла
    if k == 1:
        line = (max_width - k) * " " + min_width * "*"      #формирую первую строку кристалла с учетом минимальной ширины
    else:
        line = (max_width - k) * " " + "*"          #формирую пустые символы в начале строки, в конце добавляю *, для формирования первой половины трехугольника

    for i in range(1, k):                #заполняю пробелами первую половину трехугольника
        line += " "

    for j in range(k + min_width - 1, 1, -1):            #заполняю пробелами вторую половину трехугольника
        line += " "
    if k != 1:                          #если первая строка то не вывожу лишний *, если не первая то вывожу в конце строки * для формирования кристалла
        print(line + "*")
    else:
        print(line)

for k in range(max_width - 1, 0, -1):                #формирую столбцы для второй половины кристалла
    if k == 1:
        line = (max_width - k) * " " + min_width * "*"          #формирую первую строку кристалла с учетом минимальной ширины
    else:
        line = (max_width - k) * " " + "*"               #формирую пустые символы в начале строки, в конце добавляю *, для формирования второй половины трехугольника

    for i in range(k, 1, -1):                #заполняю пробелами первую половину трехугольника
        line += " "

    for j in range(1, k + min_width - 1):            #заполняю пробелами вторую половину трехугольника
        line += " "
    if k != 1:                              #если первая строка то не вывожу лишний *, если не первая то вывожу в конце строки * для формирования кристалла
        print(line + "*")
    else:
        print(line)

