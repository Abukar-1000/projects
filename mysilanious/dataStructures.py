# 
from io import DEFAULT_BUFFER_SIZE
import random
from tkinter import Button, Entry, Label, StringVar, Tk

gameBoard = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

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
            self.button_gui['text'] = 'X'

        def offButton(event):
            self.button_gui['background'] = self.bgColor
            self.button_gui['foreground'] = self.fgColor
            self.button_gui['text'] = ' '   

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

        self.updateButton = Button(self.window,width=15,text='Switch',bg='#C70039',fg='#DAF7A6',command=self.changeTurn)
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
        
        self.window.bind('<Enter>',refreshScreen)   # triggered if the mouse is inside the app   

    def setRandomPlayer(self):
        randomPlayer = random.choice(['player','comp'])
        self.lableVar.set(randomPlayer)

    def changeTurn(self):

        if self.lableVar.get() == 'comp':
            self.lableVar.set('player')
        elif self.lableVar.get() == 'player':
            self.lableVar.set('comp')          

    
    def compIsChoosing(self):
        choice = random.randint(0,5)
        gameBoard[choice] = 'O'
        self.updateScreen() 
        self.lableVar.set('player')
        
    def playerIsChoosing(self):
        for button in self.allButtons:
            self.effects()
            button.playerChooses()     
        self.lableVar.set('comp') 

    def main(self):
        
        if self.lableVar.get() == 'comp':
            self.compIsChoosing()
            self.updateScreen()
            self.lableVar.set('player')
        elif self.lableVar.get() == 'player':
            self.effects()
            self.playerIsChoosing()
            self.lableVar.set('comp')

display = Display()
display.lableVar.set('comp')
while True:
    display.main()
    display.show()


























# def validMove():
#     answer = 0
#     for index in gameBoard:
#         if index == ' ':
#             answer += 1
#     return answer        

# available = gameBoard.count(' ')
# gameBoard[1] = 'X'
# new = gameBoard.count(' ')

# if available > new:
#     print(True)

# print(available - 1 )


# # txtValue = StringVar()
# # txtbx = Entry(self.window,width=25)
# # txtbx.grid()
