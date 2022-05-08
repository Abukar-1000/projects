


gameBoard = ['X',' ',' ',' ',' ',' ','X',' ',' ']  # game board 
winningCombos = [
            # horizontal winning combos
            (0,1,2),
            (3,4,5),
            (6,7,8),
            # Vertical winning combos
            (0,3,6),
            (1,4,7),
            (2,5,8),
            # diagnal winning combos 
            (0,4,8),
            (2,4,6),
        ]

def checkPlayer():  # chacks if the player is about to win
        buttonToSabatoge = 0
        aboutToWin = False 
        comboIndex = 0 
        index = 0
        for combos in winningCombos:
            counter = 0
            for combo in combos:
                if gameBoard[combo] == 'X':
                    counter += 1
                if (counter/3) > .5:
                    aboutToWin = True
                    comboIndex = index
            index += 1        
        return aboutToWin,comboIndex                        
print(checkPlayer())        