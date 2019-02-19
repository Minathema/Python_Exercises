import random

def exercise18():
    print ('Welcome to the Cows and Bulls Game')
    num = random.randint(1000,9999)
    num = list(str(num))
    # print (num)
    condition = False
    tries = 0

    while condition == False:
        guess = input('Guess the 4-digit number: ')
        guess = list(guess)
        tries += 1
        if guess == num:
            print ('You are correct!')
            print ('Number of guesses:',tries)
            condition = True
        else:
            cows = 0
            bulls = 0
            for i in range(0,4):
                if guess[i] in num:
                    if guess[i] == num[i]:
                        cows += 1
                    else:
                        bulls += 1
            print ('Cows:',cows,'Bulls:',bulls)



exercise18()
