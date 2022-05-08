'''
create the game board 
create button class
create player class
create rules to see if the game is over 
create a gui 
create a hueristic algorithm

0   1   2   <-- game grid 
3   4   5
6   7   8

the board should be one array 
create a function that goes to the index of board and changes the value 

add a reset button 
and a bbutton indicating whos turn it is 

isClicked updates the game board 
store the buttons in a list 
itterate through them and update the values at the beginning of the game 

make a while loop during the game for selecting the during the game loop

game structure:

update display first
check for winners
let computer judge the game
let players make their move

'''

from tkinter import Button, StringVar, Tk, Label, messagebox
import random
import time

gameBoard = [' ']*9  # game board 
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

    def playerChoiceCheck(self,occurences): # checks if we have less available spaces in game board
        new = gameBoard.count(' ')
        if occurences > new:
            return True

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
                elif gameBoard[combo] == ' ':
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
      
            index += 1

        # finding buttons that can lead to a win based on the current button
        index = 0    
        for value in self.gameBoardValues:
            if gameBoard[index] == 'O': # if a button value is equal to o
                self.unusable.append(index)
                # self.positions.append(index)
                
                for combo in winningCombos: # itterate through winning combos 
                    if index in combo: # finds a combo where the current button is part of 
                        realtedPositions = tuple([x for x in combo if gameBoard[x] != 'X' and x != index and x not in self.unusable]) # quick check to get the buttons that that can lead to a win
                        updatingForComp.append(realtedPositions) # adds results to update             
            index += 1  

        for values in updatingForComp:      
            for value in values:
                self.gameBoardValues[value] += 99

        for values in self.unusable:
            self.gameBoardValues[values] -= 1000
        updatingForComp.clear()      
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
            print(f'the choice is {answer}') 
            gameBoard[answer] = self.character      # completes the combo
        elif playerAboutToWin == True:              # checks if player is about to win
            answer = self.findIndex(pComboIndex,'X')    # find the index needed foe player to win
            print(f'the choice is {answer}') 
            self.positions.append(answer)               # adds to position
            gameBoard[answer] = self.character          # sabotoges the win for player
        else:                                           # select best move from heuristics 
            choice = max(self.gameBoardValues)          # find highest value 
            answer = max(findMach(choice,self.gameBoardValues))   # find the most recent index of that value in game board values 
            self.positions.append(answer)               # adds to position
            print(f'the choice is {answer}')              
            gameBoard[answer] = self.character          # set the value                    
        
# conditions for each game 
        
def checkForWin(player):  # checks if player has completed a combo returns True/False
    playerHasWon = False
    for combos in winningCombos:
        counter = 0
        for value in combos:
            if value in player.positions:
                counter += 1      
        if (counter/3) == 1:        
            playerHasWon = True
            return playerHasWon   

def checkForWinUsingCharacter(character):   # checks if player has completed a combo returns True/False based on a charcter passed in
    playerHasWon = False
    for combos in winningCombos:
        counter = 0
        for value in combos:
            if value == character:
                counter += 1      
        if (counter/3) == 1:        
            playerHasWon = True
            return playerHasWon         

def checkForDraw(): # checks if niether player won, and that there is no available plays left, return True/False
    if gameBoard.count(' ') == 0:
        return True
    return False     


#               createing the GUI  



class BoardButtons():

    def __init__(self,display,number,bgColor,fgColor,column,row,func = None):
        self.buttonNumber = number # identifies which button it is 
        self.value = gameBoard[self.buttonNumber]   # a button displays gameboard at a given index
        self.fgColor = fgColor
        self.bgColor = bgColor
        self.button_gui = Button(display,text=self.value,bg=self.bgColor,fg=self.fgColor,width = 10,command=func)  # button gui properties
        self.button_gui.grid(column=column,row=row,padx=5,pady=5)   # allows the button to be arranged during initialization  

    def updateValue(self):  # updates what the button if game board index is updated 
        self.button_gui['text'] = gameBoard[self.buttonNumber]  

    def clickButton(self): # allows computer to click a button
        self.button_gui.invoke() 

    def hover(self):  

        def overButton(event):  
            self.button_gui['background'] = self.fgColor
            self.button_gui['foreground'] = self.bgColor


        def offButton(event):
            self.button_gui['background'] = self.bgColor
            self.button_gui['foreground'] = self.fgColor

        self.button_gui.bind('<Enter>',overButton) 
        self.button_gui.bind('<Leave>',offButton)  

    def playerChooses(self):    # functionality to allow player to click a button

        def playerClick(event): # function to execut click
            if gameBoard[self.buttonNumber] == ' ': # checks if the button has no value
                gameBoard[self.buttonNumber] = 'X'  # assigns player value 
                self.updateValue()   # updates button text 

        self.button_gui.bind('<Button-1>',playerClick)     # event is triggered if the button is clicked with the left mouse button      



class Display():

    def __init__(self):
        self.comp = Computer()
        self.window = Tk()
        self.window.configure(background='#000000')
        self.window.geometry('600x600')
        self.window.title('tic tac toe')
        # creating buttons 
        self.button0 = BoardButtons(self.window,0,bgColor='#C70039',fgColor='#DAF7A6',column=0,row=0,func=self.main)
        self.button1 = BoardButtons(self.window,1,bgColor='#C70039',fgColor='#DAF7A6',column=1,row=0,func=self.main)
        self.button2 = BoardButtons(self.window,2,bgColor='#C70039',fgColor='#DAF7A6',column=2,row=0,func=self.main)
        
        self.button3 = BoardButtons(self.window,3,bgColor='#C70039',fgColor='#DAF7A6',column=0,row=1,func=self.main)
        self.button4 = BoardButtons(self.window,4,bgColor='#C70039',fgColor='#DAF7A6',column=1,row=1,func=self.main)
        self.button5 = BoardButtons(self.window,5,bgColor='#C70039',fgColor='#DAF7A6',column=2,row=1,func=self.main)

        self.button6 = BoardButtons(self.window,6,bgColor='#C70039',fgColor='#DAF7A6',column=0,row=2,func=self.main)
        self.button7 = BoardButtons(self.window,7,bgColor='#C70039',fgColor='#DAF7A6',column=1,row=2,func=self.main)
        self.button8 = BoardButtons(self.window,8,bgColor='#C70039',fgColor='#DAF7A6',column=2,row=2,func=self.main)

        self.allButtons = (self.button0,self.button1,self.button2,
        self.button3,self.button4,self.button5,
        self.button6,self.button7,self.button8
        )

        self.updateButton = Button(self.window,width=15,text='refresh',bg='#C70039',fg='#DAF7A6')
        self.updateButton.grid(column=4,row=1)
        
        self.lableVar = StringVar()
        self.current = Label(self.window,width=15,textvariable=self.lableVar)
        self.current.grid(column=4,row=0)

    def show(self):
        self.window.mainloop()   

    def effects(self):
        for button in self.allButtons:
            button.hover()

    def updateScreen(self):     # refreshes all the buttons on the screen 

        def refreshScreen(event):
            for button in self.allButtons:  
                button.updateValue()
        
        self.updateButton.bind('<Button-1>',refreshScreen)   # triggered if the mouse is inside the app   

    def setRandomPlayer(self):
        randomPlayer = random.choice(['player','comp'])
        self.lableVar.set(randomPlayer)

    def changeTurn(self):

        if self.lableVar.get() == 'comp':
            self.lableVar.set('player')
        elif self.lableVar.get() == 'player':
            self.lableVar.set('comp')          

    
    def compIsChoosing(self):
        self.comp.updatePositionValues()
        self.comp.selectButton()
        self.updateScreen()
        self.lableVar.set('player')

        
    def playerIsChoosing(self):
        availableSpots = gameBoard.count(' ')
        for button in self.allButtons:
            self.updateScreen()
            self.effects()
            button.playerChooses()     
        self.lableVar.set('comp')

    def main(self):
        
        if checkForWin(self.comp) == True:
            messagebox.askyesno('game over','Computer has Won!\nDo you want to play again')
        elif checkForWinUsingCharacter('X') == True:
            messagebox.askyesno('game over','You Won!!!\nDo you want to play again') 
        elif checkForDraw() == True:
            messagebox.askyesno('game over','Game is a Draw \nDo you want to play again')
        elif self.lableVar.get() == 'comp':
            self.compIsChoosing()
        elif self.lableVar.get() == 'player':
            self.playerIsChoosing()
                 

                



# p = Player()
# comp = Computer()
display = Display() 
display.lableVar.set('comp')
while True:
    display.main()
    display.show()
        
# appOn = True
# gameOn = True

               
    