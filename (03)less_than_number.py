def exercise3():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []
    for x in a:
        if x < 5 :
            b.append(x)
    print (b)

    num = input('Please pick a number: ')
    c = []
    for y in a:
        if y < int(num):
            c.append(y)
    print (c)


exercise3()
