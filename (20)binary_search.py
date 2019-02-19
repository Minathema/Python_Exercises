def exercise20(the_list,num):
    mid = int(len(the_list)//2)
    first = 0
    last = len(the_list) - 1
    condition = False

    if num == mid:
        condition = True
    else:
        while condition == False and first < mid and last > mid:
            if num > mid:
                if the_list[last] == num:
                    condition = True
                else:
                    last -= 1
            elif num < mid:
                if the_list[first] == num:
                    condition = True
                else:
                    first += 1

    print (condition)


exercise20([2,5,6,7,8,9,10,11,13,14,15],13)
