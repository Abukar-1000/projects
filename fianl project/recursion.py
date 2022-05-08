
from tkinter import Button,Tk, Entry 
import random
import time
# # return a fibinachi number based on its index (x)
# def fib(x):
#     if x <= 2:
#         return 1
#     else:
#         return fib(x-1) + fib(x-2)

# # print(fib(9))     

# # return the combined value of each digit in a number 1234 --> 10
# def recSum(x):
#     if x <= 1:
#         return x
#     else:
#         return int(x%10 + recSum(x/10))

# # print(recSum(1234))

# # check if you can make the phrase from a given wordlist recursively
# def wordSplit(phrase,wordList,output = []):
#     pass

def update(button):
    button['text'] = values[0]

values = [str(x) for x in range(0,9)]
window = Tk()
window.configure(background="silver")
window.geometry('600x600')

class BoardButtons():

    def __init__(self,display,number,bgColor,fgColor,column,row,func):
        self.buttonNumber = number # identifies which button it is 
        self.value = values[self.buttonNumber]   # button data type
        self.button_gui = Button(display,text=self.value,bg=bgColor,fg=fgColor,width = 10,command=func)  # button gui properties
        self.button_gui.grid(column=column,row=row,padx=5,pady=5)   # allows the button to be arranged during initialization  

    
    def updateStuff(self):
        self.button_gui.invoke()


def updateValue(button):
        value = random.choice(['X','O'])
        values[button.buttonNumber] = value
        button.button_gui['text'] = values[button.buttonNumber] 

button0 = BoardButtons(window,0,bgColor='black',fgColor='green',column=0,row=1,func = lambda:updateValue(button0))    
button1 = BoardButtons(window,1,bgColor='black',fgColor='green',column=1,row=1,func = lambda:updateValue(button1))  

buttons = (button0,button1)

def UpdateAllButtons():
    for button in buttons:
        button.updateStuff()

updateButton = Button(window,text="Update Button",bg='silver',fg='silver',command=UpdateAllButtons)
updateButton.grid(column=0,row=6)

while True:
    updateButton.value = "UpdateButton"
    window.mainloop()
    

    









































# while True:
#     window.mainloop()
#     change = input("value:  ")
#     change = int(change)
#     values[change] = input('insert new vlaue:   ') 
#     button0.updateValue()