def exercise13():
    numbers = input('How many Fibonnaci numbers would you like? ')
    numbers = int(numbers)
    a = [1,1]
    z = 1
    if numbers != 0 :
        if numbers == 1:
            print ([1])
        elif numbers == 2:
            print (a)
        else:
            for y in range(numbers-2):
                w = a[z] + a[z-1]
                a.append(w)
                z += 1
            print (a)


exercise13()
