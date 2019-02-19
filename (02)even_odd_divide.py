def exercise2():
    number1 = input('Please pick a number: ')
    if int(number1) % 4 == 0 :
        print (number1,'is an even number and a multiple of 4')
    elif int(number1) % 2 == 0 :
        print (number1,'is an even number')
    else :
        print (number1,'is an odd number')

    num = input('Please pick one more number: ')
    check = input('And another one: ')
    if int(num) % int(check) == 0 :
        print (check,'divides evenly into',num)
    else :
        print (check,'does not divide evenly into',num)


exercise2()
