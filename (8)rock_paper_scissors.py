def exercise8():
    new_game = 'Yes'
    while new_game == 'Yes':
        plays = input('How many times would you like to play? ')
        win1 = 0
        win2 = 0
        plays = int(plays)
        while plays > 0:
            player1 = input('Player 1 picks: Rock, Paper or Scissors? ')
            player2 = input('Player 2 picks: Rock, Paper or Scissors? ')
            if player1 == player2 :
                print ('This match is a draw')
            elif player1 == 'Rock' :
                if player2 == 'Paper':
                    win2 += 1
                    print ('Paper covers Rock')
                elif player2 == 'Scissors':
                    win1 += 1
                    print ('Rock smashes Scissors')
            elif player1 == 'Paper':
                if player2 == 'Rock':
                    win1 += 1
                    print ('Paper covers Rock')
                elif player2 == 'Scissors':
                    win2 += 1
                    print ('Scissors cut Paper')
            elif player1 == 'Scissors':
                if player2 == 'Rock':
                    win2 += 1
                    print ('Rock smashes Scissors')
                elif player2 == 'Paper':
                    win1 += 1
                    print ('Scissors cut Paper')
            plays -= 1

        if win1 > win2 :
            print ('Player 1 wins the game')
        elif win2 > win1 :
            print ('Player 2 wins the game')
        else:
            print ('The game results in a draw')

        new_game = input('Would you like to start another game? ')

    print ('End of Game')


exercise8()
