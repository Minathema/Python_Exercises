import random

def exercise14(length):
    list1 = []
    for i in range(length):
        x = random.randint(0,40)
        list1.append(x)
    print (list1)

    list2 = set(list1)
    print (list2)


exercise14(20)
