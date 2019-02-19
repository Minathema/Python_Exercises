import random

def exercise16():
    condition_1 = False

    while condition_1 == False :
        print ('The password should contain at least 4 characters.')
        length = input('How many characters would you like your password to have? ')
        length = int(length)
        if length >= 4:
            condition_1 = True

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    punct = "@%+#/'!$\^?:,()[]}{~`-_."
    condition_2 = False

    while condition_2 == False:
        password = []
        count_numbers = 0
        count_lower = 0
        count_caps = 0
        count_symbols = 0
        for x in range(length):
            y = random.randint(1,3)
            if y == 1:
                char = random.randint(0,9)
                count_numbers += 1
            elif y == 2:
                z = random.randint(1,2)
                if z == 1:
                    char = alphabet[random.randint(0,25)]
                    count_lower += 1
                else:
                    char = (alphabet[random.randint(0,25)]).upper()
                    count_caps += 1
            else:
                char = punct[random.randint(0,23)]
                count_symbols += 1
            password.append(str(char))
        if count_numbers >= int(length//4) and count_lower >= int(length//4) \
        and count_caps >= int(length//4) and count_symbols >= int(length//4):
            condition_2 = True

    print ("Your new password is: ", ''.join(password))


exercise16()
