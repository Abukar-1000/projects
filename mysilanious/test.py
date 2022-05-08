

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
gameBoard = [' ',' ',' ',' ',' ',' ',' ',' ',' ']  # game board 
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


class Player():

    def __init__(self):
        self.character = 'X'
        self.positions = []


class Computer(Player):

    def __init__(self):
        Player.__init__(self) 
        self.character = 'O'    # Computers character 
        self.gameBoardValues = [3,2,3,2,4,2,3,2,3] # numeric reprisentation of each buttons worth 
        self.unusable = [] # buttons that have already been clicked

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
                        realtedPositions = ([x for x in combo if gameBoard[x] != 'O' and x != index]) # quick check to get the buttons that that can lead to a win
                        updatingForPlayer.append(realtedPositions) # adds results to update
            index += 1

        index = 0    
        for value in self.gameBoardValues:
            if gameBoard[index] == 'O': # if a button value is equal to o
                self.unusable.append(index)
                self.positions.append(index)
                # finding buttons that can lead to a win based on the current button
                for combo in winningCombos: # itterate through winning combos 
                    if index in combo: # finds a combo where the current button is part of 
                        realtedPositions = ([x for x in combo if gameBoard[x] != 'X' and x != index and x not in self.unusable]) # quick check to get the buttons that that can lead to a win
                        updatingForComp.append(realtedPositions) # adds results to update             
            index += 1    

        # update heuristic values for computer 
          



    def selectButton(self):
        choice = [x for x in range(0,9) if x not in self.unusable]
        bestMatch = [0.0,0] # decimal evaluation of each combo, index of the best match
        result = bestMatch[1]
        index = 0
        for combos in winningCombos:
            counter = 0
            for combo in range(3):
                if combos[combo] in self.positions and choice:
                    counter += 1
                if (counter/3) > bestMatch[0]:
                    bestMatch[0] = counter/3
                    bestMatch[1] = index
                index += 1  

        gameBoard[result] = 'O'        


comp = Computer()
current = random.choice(['comp','player'])






for x in range(9):
    print(current)
    if current == 'comp':
        print(gameBoard)
        print(comp.gameBoardValues)
        comp.updatePositionValues()
        comp.selectButton()
        print(gameBoard)
        print(comp.gameBoardValues)
        current = 'player'
    else:     
        question = int(input("index:    "))
        gameBoard[question] = "X"
        current = 'comp'


# for values in updatingForComp:
#             print(values)
#             for value in values:
#                 self.gameBoardValues[value] += 99   

#         for values in updatingForPlayer:
#             print(f'{values}',end=" ")
#             for value in values:
#                 self.gameBoardValues[value] -= 99