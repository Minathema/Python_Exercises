def exercise6():
    sentence = input('Please pick a sentence: ')
    sent1 = []
    for x in sentence:
        if x.isalpha() == True:
            sent1.append(x.lower())

    if sent1 == list(reversed(sent1)):
        print ('This sentence is a palindrome')
    else:
        print ('This sentence is not a palindrome')

exercise6()
