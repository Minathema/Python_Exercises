from math import sqrt

def exercise11():
    num = input('Please pick a number: ')
    num = int(num)
    if num == 1 or num == 0 :
        print (num,'is neither a prime nor a composite number')
    elif num == 2 or num == 3 :
        print (num, 'is a prime number') 
    else:
        for x in range(2, int(sqrt(num)) + 1):
            if num % x == 0 :
                print (num,'is not a prime number')
                break
            else:
                if x == int(sqrt(num)) :
                    print (num,'is a prime number')


exercise11()
