import random

def exercise9():
    num = random.randint(1,9)
    guesses = 0
    print ('You can stop the game by typing "exit"')
    g_num = input('Guess the secret number: ')
    while g_num != 'exit':
        if int(g_num) == num:
            print ('Yay, you found it!')
            break
        elif int(g_num) > num:
            print (g_num,'is higher than the secret number')
        else:
            print (g_num,'is lower than the secret number')
        guesses += 1
        g_num = input('Guess the secret number: ')
    print ('You took',guesses,'guesses')


exercise9()
