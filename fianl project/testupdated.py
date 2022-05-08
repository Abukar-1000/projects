

# best_match = [0.0,0]
# current_combo = 0

# # chooses a combo to complete 
# for combo in winning_combo:
#     counter = 0
#     for position in combo:
#         if position in answers:
#             counter += 1
#         if (counter/3) > best_match[0]:
#             best_match[0] = (counter/3)
#             best_match[1] = current_combo
#     current_combo += 1  

# spot = best_match[1]
# # Finds the indicies needed to complete 
# choice = 0
# for index in winning_combo[spot]:
#     if index not in answers:
#         choice = index    
    
# print(winning_combo[spot])
# print(choice)



''''
update the values of each button based on who has it
figure out which buttons can be used to complete a combo 
make their value and the values of corisponding buttons higher 
choose a button based on the highest value
H V 
'''
# winning_combo = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
# gameBoard = ['o',' ',' ',' ','x',' ',' ',' ',' ']
# gameBoardValues = [3,2,3,2,4,2,3,2,3]
# answers = [0,2,3,5]


            


# # print(gameBoard)  
# print(f"comp: {updatingForComp}\nplayer: {updatingForPlayer}")
# print(gameBoardValues)      

# counter = 0 # sets a counter to step through values 
#         for value in game_board:    # itterating through game board
#             if game_board[counter] == "O":  # check if it is an O
#                 self.positions.append(counter)  # add it to positions
#             elif game_board[counter] == "X":  # check if the position has X
#                 if self.gameBoardValues[counter] != -10: # check if the same position in gameBoardValues is -10
#                     self.gameBoardValues[counter] = -10 # if not, update the value to -10
#             counter += 1  # changes the index

# update for best match based on winning combos 
#         best_match_index = 0
#         highest_match = 0
#         current_index = 0
#         for combos in winningCombos:
#             print(f"Index{current_index}")
#             match = 0
#             for combo in combos:
#                 print(combo)
#                 if combo in self.positions:
#                     match += 1
#             match = match/3
#             if match > highest_match:
#                 highest_match = match
                       
                    
#             current_index += 1

'''
0   1   2
3   4   5
6   7   8
'''

import random
from tkinter import Button, Spinbox, StringVar, Tk
from typing import Counter
gameBoard = ['','','','','','','','','']  # game board 
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

def findMach(value,variable): # returns all indicies where a value is found in an object
    answer = []
    index = 0
    for stuff in variable: # loop through elements
        if stuff == value:   # check if the element is in the variable 
            answer.append(index)    # add to answers
        index += 1    

    if len(answer) >= 1:    # check if we have answers
        return answer       # returns answers 
    else:
        return -1        # signifies no answers 



class Player():

    def __init__(self):
        self.character = 'X'
        self.positions = []

    def UpdatePositions(self):  #updates the positions the player holds 
        index = 0
        for spot in gameBoard:    
            if spot == self.character:
                if index not in self.positions:
                    self.positions.append(index)
            index += 1

class Computer(Player):

    def __init__(self):
        Player.__init__(self) 
        self.character = 'O'    # Computers character 
        self.gameBoardValues = [3,2,3,2,4,2,3,2,3] # numeric reprisentation of each buttons worth 
        self.unusable = [] # buttons that have already been clicked

    def checkPlayer(self,character):  # chacks if a combo is about to be completed 
        aboutToWin = False 
        comboIndex = ()
        index = 0
        for combos in winningCombos:
            xValue = 0
            spaces = 0
            for combo in combos:
                if gameBoard[combo] == character:
                    xValue += 1
                elif gameBoard[combo] == '':
                    spaces += 1    
            if (xValue/3) > .5 and spaces == 1:
                aboutToWin = True
                comboIndex = index
            index += 1        
        return (aboutToWin,comboIndex)     
    
    def findIndex(self,index,value):    # given a combo, inserts a value to complete it
        answer = 0                          # index to return 
        for spot in winningCombos[index]:   
            if gameBoard[spot] != value:    # check to find the spot missing 
                answer = spot               # set the spot as our answer 
        # winningCombos.pop(index)            # remove combo since it cant be completed anymore
        return answer

    def updatePositionValues(self): # updates the numeric values of each spot on game board 
        updatingForComp = [] # tuple of positions related to the computer indicies that will be updated
        updatingForPlayer = [] # tuple of positions related to the player indicies that will be updated

        index = 0
        for value in self.gameBoardValues:
            if gameBoard[index] == 'X':
                self.unusable.append(index)
                # finding buttons that can lead to a win based on the current button
                for combo in winningCombos: # itterate through winning combos 
                    if index in combo: # finds a combo where the current button is part of 
                        realtedPositions = tuple([x for x in combo if gameBoard[x] != 'O' and x != index]) # quick check to get the buttons that that can lead to a win
                        updatingForPlayer.append(realtedPositions) # adds results to update
            index += 1

        index = 0    
        for value in self.gameBoardValues:
            if gameBoard[index] == 'O': # if a button value is equal to o
                self.unusable.append(index)
                # self.positions.append(index)
                # finding buttons that can lead to a win based on the current button
                for combo in winningCombos: # itterate through winning combos 
                    if index in combo: # finds a combo where the current button is part of 
                        realtedPositions = tuple([x for x in combo if gameBoard[x] != 'X' and x != index and x not in self.unusable]) # quick check to get the buttons that that can lead to a win
                        updatingForComp.append(realtedPositions) # adds results to update             
            index += 1  

        for values in updatingForComp:      
            for value in values:
                self.gameBoardValues[value] += 99

        for values in self.unusable:
            self.gameBoardValues[values] -= 100
        updatingForComp.clear()
        updatingForPlayer.clear()        
        # update heuristic values for computer 


    def selectButton(self):
        # check if computer can win 
        # sabotage player 
        # or select a value from heuristics 
        answer = 0  # index to select in game board
        compAboutToWin,comboIndex = self.checkPlayer(character='O')     # checking if computer is about to win, returns combo associated 
        playerAboutToWin,pComboIndex = self.checkPlayer(character='X')  # checking if player is about to win, returns combo associated 

        # prioritize computer win
        if compAboutToWin == True:        
            answer = self.findIndex(comboIndex,'O') # find index needed for combuter to win
            self.positions.append(answer)           # add to positions
            gameBoard[answer] = self.character      # completes the combo
        elif playerAboutToWin == True:              # checks if player is about to win
            answer = self.findIndex(pComboIndex,'X')    # find the index needed foe player to win
            self.positions.append(answer)               # adds to position
            gameBoard[answer] = self.character          # sabotoges the win for player
        else:                                           # select best move from heuristics 
            choice = max(self.gameBoardValues)          # find hiest value 
            answer = max(findMach(choice,self.gameBoardValues))   # find the most recent index of that value in game board values 
            self.positions.append(answer)               # adds to position
            print(f'the choice is {answer}')              
            gameBoard[answer] = self.character          # set the value                    
        

def checkForWin(player):
    playerHasWon = False
    for combos in winningCombos:
        counter = 0
        for value in combos:
            if value in player.positions:
                counter += 1      
        if (counter/3) == 1:        
            playerHasWon = True
            return playerHasWon   

def showBoard():
    print(f'{gameBoard[0]}  {gameBoard[1]}  {gameBoard[2]}\n{gameBoard[3]}  {gameBoard[4]}  {gameBoard[5]}\n{gameBoard[6]}  {gameBoard[7]}  {gameBoard[8]}'
    )
comp = Computer()
p = Player()

appOn = True
GameOn = True

while appOn:
    current = random.choice(['comp','player'])
    while GameOn:
        if checkForWin(comp) == True:
            print('computer has won')
            GameOn = False
        elif checkForWin(p) == True:
            print('Player has won!!!')
            GameOn = False    
        elif current == 'comp':
            print(checkForWin(comp))
            comp.updatePositionValues()
            comp.selectButton()
            showBoard()
            print(comp.gameBoardValues)
            current = 'player'
        elif current == 'player':
            p.UpdatePositions()
            spot = input('index: ')
            spot = int(spot)
            gameBoard[spot] = 'X'
            current = 'comp'
    print('first game has ended') 
    appOn = False       
print(gameBoard)

# for values in updatingForComp:
#             print(values)
#             for value in values:
#                 self.gameBoardValues[value] += 99   

#         for values in updatingForPlayer:
#             print(f'{values}',end=" ")
#             for value in values:
#                 self.gameBoardValues[value] -= 99


# choice = [x for x in range(0,9) if x not in self.unusable]
#         bestMatch = [0.0,0] # decimal evaluation of each combo, index of the best match
#         result = bestMatch[1]
#         index = 0
#         for combos in winningCombos:
#             counter = 0
#             for combo in range(3):
#                 if combos[combo] in self.positions and choice:
#                     counter += 1
#                 if (counter/3) > bestMatch[0]:
#                     bestMatch[0] = counter/3
#                     bestMatch[1] = index
#                 index += 1  

#         gameBoard[result] = 'O'  


# self.gameBoardValues
#         highest = 0
#         index = 0
#         counter = 0
#         for x in self.gameBoardValues:
#             if x >= highest:
#                 highest = x
#                 index = counter
#             counter += 1
#         gameBoard[index] = self.character  





# if playerAboutToWin == False:
#             choice = max(self.gameBoardValues)
#             spot = max(findMach(choice,self.gameBoardValues))
#             print(f'the choice is {spot}')
#             gameBoard[spot] = self.character
#         else:
#             choice = 0
#             print(f"sabotoging combo blocked: {index}")
#             for spot in winningCombos[index]:
#                 if gameBoard[spot] != 'X':
#                     choice = spot 
#             winningCombos.pop(index)  
#             gameBoard[choice] = self.character











# old class

# class Computer(Player):

#     def __init__(self):
#         Player.__init__(self) 
#         self.character = 'O'    # Computers character 
#         self.gameBoardValues = [3,2,3,2,4,2,3,2,3] # numeric reprisentation of each buttons worth 

#     def updatePositionValues(self): # updates the numeric values of each spot on game board 
#         counter = 0 # sets a counter to step through values 
#         for value in game_board:    # itterating through game board
#             if game_board[counter] == "O":  # check if it is an O
#                 self.positions.append(counter)  # add it to positions
#             elif game_board[counter] == "X":  # check if the position has X
#                 if self.gameBoardValues[counter] != -10: # check if the same position in gameBoardValues is -10
#                     self.gameBoardValues[counter] = -10 # if not, update the value to -10
#             counter += 1  # changes the index 
        
        

#     def selectButton(self):
#         # update for best match based on winning combos 
#         best_match_index = 0
#         highest_match = 0
#         current_index = 0
#         for combos in winningCombos:
#             print(f"Index{current_index}")
#             match = 0
#             for combo in combos:
#                 print(combo)
#                 if combo in self.positions:
#                     match += 1
#             match = match/3
#             if match > highest_match:
#                 highest_match = match
                       
                    
#             current_index += 1


# while gameOn:
#         if checkForWin(p) == True:
#             gameOn = False
#         elif checkForWin(comp) == True:
#             gameOn = False
#         elif current == 'player':   # make sure the player has an update button
#             display.updateEntry('current')
#             options = gameBoard.count(' ')
#             choosing = True
#             while choosing:
#                 if p.playerChoiceCheck(options) == True:
#                     choosing = False
#             current = 'comp'
#         elif current == 'comp':
#             display.updateEntry('current')
#             comp.updatePositionValues()
#             comp.selectButton()
#             print(gameBoard) 
#             current = 'player'           


# def switch(event):
#             if self.lableVar.get() == 'comp':
#                 self.lableVar.set('player')
#                 print(self.lableVar.get())
#             elif self.lableVar.get() == 'player':
#                 self.lableVar.set('comp') 
#                 print(self.lableVar.get())  

#         self.updateButton.bind('<Button-1>',switch)     