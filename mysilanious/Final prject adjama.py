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

from tkinter import Button, Spinbox, StringVar, Tk
import random

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

class BoardButtons():

    def __init__(self,display,number,index,bgColor,fgColor,column,row,func):
        self.buttonNumber = number # identifies which button it is 
        self.value = StringVar()    # button data type
        self.button_gui = Button(display,text = ' ',bg=bgColor,fg=fgColor,width = 10,command=func)  # button gui properties
        self.button_gui.grid(column=column,row=row,padx=5,pady=5)   # allows the button to be arranged during initialization  

    def updateValue(self,number):
        self.button_gui['text'] = f'{gameBoard[number]}'

    def computerPushButton(self):
        self.button_gui.invoke()    

class Player():

    def __init__(self):
        self.character = 'X'
        self.positions = []


class Computer(Player):

    def __init__(self):
        Player.__init__(self) 
        self.character = 'O'    # Computers character 
        self.gameBoardValues = [3,2,3,2,4,2,3,2,3] # numeric reprisentation of each buttons worth 

    def updatePositionValues(self): # updates the numeric values of each spot on game board 
        updatingForComp = [] # tuple of positions related to the computer indicies that will be updated
        updatingForPlayer = [] # tuple of positions related to the player indicies that will be updated

        index = 0
        for value in self.gameBoardValues:
            if gameBoard[index] == 'X':
                self.gameBoardValues[index] -= 99 # reduse values where the buttons value is x 
                # finding buttons that can lead to a win based on the current button
                for combo in winningCombos: # itterate through winning combos 
                    if index in combo: # finds a combo where the current button is part of 
                        realtedPositions = tuple([x for x in combo if gameBoard[x] != 'O' and x != index]) # quick check to get the buttons that that can lead to a win
                        if len(realtedPositions) > 1: # if the len of realted positions is 1, then one of the values had an x and cant lead to a win
                            updatingForPlayer.append(realtedPositions) # adds results to update
            index += 1

        index = 0    
        for value in self.gameBoardValues:
            if gameBoard[index] == 'O': # if a button value is equal to o
                # finding buttons that can lead to a win based on the current button
                for combo in winningCombos: # itterate through winning combos 
                    if index in combo: # finds a combo where the current button is part of 
                        realtedPositions = tuple([x for x in combo if gameBoard[x] != 'X' and x != index]) # quick check to get the buttons that that can lead to a win
                        if len(realtedPositions) > 1: # if the len of realted positions is 1, then one of the values had an x and cant lead to a win
                            updatingForComp.append(realtedPositions) # adds results to update             
            index += 1    

        # update heuristic values for computer 
        for values in updatingForComp:
            for value in values:
                self.gameBoardValues[value] += 99   

        # update heuristic values for player
        for values in updatingForPlayer:
            for value in values:
                self.gameBoardValues[value] -= 99

    def selectButton(self): # selects a button based on gameBoardValues 
        result = self.gameBoardValues.index(max(self.gameBoardValues))
        gameBoard[result] = self.character
        return result


def isClicked(button,player):
    if player.character == 'X':
        if gameBoard[button.buttonNumber] == " ":
            gameBoard[button.buttonNumber] = player.character
            button.updateValue(button.buttonNumber)
    else:
        button.updateValue(button.buttonNumber)     

class Display():

    def __init__(self):
        self.window = Tk()   # create self.window
        self.window.title("Tik Tak Toe") # self.window name
        self.window.configure(background="silver")   # background color 
        self.window.geometry("600x300")  # self.window dimensions
        self.current_player = None
        # creating buttons arrange buttons and map their indicies  
        self.button0 = BoardButtons(self.window,0,gameBoard[0],"red","yellow",2,3,lambda:isClicked(self.button0,self.current_player))
        self.button1 = BoardButtons(self.window,1,gameBoard[1],"red","yellow",3,3,lambda:isClicked(self.button1,self.current_player))
        self.button2 = BoardButtons(self.window,2,gameBoard[2],"red","yellow",4,3,lambda:isClicked(self.button2,self.current_player))
        self.button3 = BoardButtons(self.window,3,gameBoard[3],"red","yellow",2,4,lambda:isClicked(self.button3,self.current_player))
        self.button4 = BoardButtons(self.window,4,gameBoard[4],"red","yellow",3,4,lambda:isClicked(self.button4,self.current_player))
        self.button5 = BoardButtons(self.window,5,gameBoard[5],"red","yellow",4,4,lambda:isClicked(self.button5,self.current_player))
        self.button6 = BoardButtons(self.window,6,gameBoard[6],"red","yellow",2,5,lambda:isClicked(self.button6,self.current_player))
        self.button7 = BoardButtons(self.window,7,gameBoard[7],"red","yellow",3,5,lambda:isClicked(self.button7,self.current_player))
        self.button8 = BoardButtons(self.window,8,gameBoard[8],"red","yellow",4,5,lambda:isClicked(self.button8,self.current_player))
        self.window.mainloop()

    def UpdateButton(self,ButtonNumber):
        Buttons = {'0':self.button0,'1':self.button1,
        '2':self.button2,'3':self.button3,
        '4':self.button4,'5':self.button5,
        '6':self.button6,'7':self.button7,
        '8':self.button8} 
        ButtonNeeded = Buttons[str(ButtonNumber)]
        ButtonNeeded.computerPushButton()

    def setCurrentPlayer(self,player):
        self.current_player.append(player)


        




            
            

p = Player()
comp = Computer()
display = Display()

gameOn = True
while gameOn:
    display.setCurrentPlayer(comp)
    print(display.current_player)
    print(gameBoard)
  
    



               

    




# comp.updatePositionValues()
# comp.select_Button()