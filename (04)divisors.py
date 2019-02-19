def exercise4():
    list = []
    num = input('Please pick a number: ')
    for x in range(1, int(num) + 1):
        if int(num) % x == 0 :
            list.append(x)
    print (list)

exercise4()
