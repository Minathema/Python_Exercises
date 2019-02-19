import random

def exercise5():
    list1 = []
    for x in range(random.randint(5, 20)):
        list1.append(random.randint(1, 50))
    print (list1)

    list2 = []
    for y in range(random.randint(5, 20)):
        list2.append(random.randint(1, 50))
    print (list2)

    common = []
    for z in list1:
        for w in list2:
            if z == w:
                if z not in common:
                    common.append(z)

    if not common:
        print ('There are no common numbers')
    else:
        print ('The common numbers are:',common)


exercise5()
