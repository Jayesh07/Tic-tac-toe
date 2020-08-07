

# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 18:05:32 2019

@author: Jayesh
"""



from tkinter import *
import random
root1=Tk()
L1=Label(root1,text="Choose option",bg="black",fg="white",font=("Open Sans",15,'bold'))
L1.pack()
root1.title("Tic Tac Toe")
root1.geometry("500x500")
root1.configure(background="cyan")
root1.resizable(0,0)
b1=Radiobutton(root1,text="Player vs Player",value=1,width=25,height=5,font=("Open Sans",15,'bold'))
b1.pack()
b2=Radiobutton(root1,text="Player vs Computer",value=2,width=25,height=5,font=("Open Sans",15,'bold'))
b2.pack()



class MyApp(Tk):
    def __init__(self):
        
        
        Tk.__init__(self)

       
        fr = Frame(self)

      
        self.player1_button = Button(self, text="Player 1",
                                    command=lambda: self.do_start(TRUE),bg="yellow",fg="black",
                                    font=("Open Sans", 16,"bold"))
        self.player2_button = Button(self, text="Player 2",bg="yellow",fg="black",
                                      command=lambda: self.do_start(FALSE),
                                      font=("Open Sans", 16,"bold"))
        self.exit_button = Button(self, text="Exit", command=self.do_exit,bg="yellow",fg="black",
                                  font=("Open Sans", 16,"bold"))
        self.again_button = Button(self, text="again?", command=self.do_again,bg="yellow",fg="black",
                                   state=DISABLED,
                                   font=("Open Sans", 16,"bold"))
        self.myLabel = Label(self, text="Who starts?", font=("Open Sans",16,'bold'),bg="black",fg="white",)

    
        self.bList = [0,1,2,3,4,5,6,7,8,9]

        for i in range(1,10):
            self.bList[i] = Button(self, text="",  
                                   command=lambda j=i: self.do_button(j),
                                   state=DISABLED, relief=RAISED, height=3,
                                   width=7, font=("Open Sans",24,'bold'))

   
        fr.grid()
        self.myLabel.grid(row=0, columnspan=4)
        self.player1_button.grid(row=1, column=0)
        self.player2_button.grid(row=1, column=2)
        self.exit_button.grid(row=5, column=0)
        self.again_button.grid(row=5, column=2)

 
        myL = [[1,4,0], [2,4,1], [3,4,2],  
               [4,3,0], [5,3,1], [6,3,2],
               [7,2,0], [8,2,1], [9,2,2]]
        for i in myL:
            self.bList[i[0]].grid(row=i[1], column=i[2])

    def do_start(self,player):
  
        
        self.player1_button.config(state=DISABLED)
        self.player2_button.config(state=DISABLED)
        self.again_button.config(state=DISABLED)

   
        self.bState = [10,0,0,0,0,0,0,0,0,0] 
        self.mySums = [0,0,0,0,0,0,0,0]       
        self.gameDone = FALSE
        self.specialDefense = FALSE

       
        for i in range(1,10):
            self.bList[i].config(state=NORMAL)

     
     
        if player:
            self.myLabel.config(text="You are X, make a move")
            self.turn = FALSE
        else:
            self.myLabel.config(text="You are 0, make a move")
            self.turn = TRUE
           

    def do_button(self, i):
       
    
        if self.turn:
            myText = "0"
            self.myLabel.config(text="You are X, make a move")
            self.turn = FALSE
            self.bState[i] = -1
        else:
            myText = "X"
            self.myLabel.config(text="You are 0, make a move")
            self.turn = TRUE
            self.bState[i] = 1

 
        self.bList[i].config(text=myText, state=DISABLED)
        self.test_done()

       
   
    def test_done(self):
       
   
        if not (0 in self.bState):
            self.myLabel.config(text="Draw!")
         
            self.again_button.config(state=NORMAL)

    
        self.do_sums()
        if 3 in self.mySums: 
            self.myLabel.config(text="Player 1 won!")
          
            for i in range(1,10):
                if self.bState[i] == 0:
                    self.bList[i].config(text="", state=DISABLED)
            self.gameDone = TRUE 
            
            self.again_button.config(state=NORMAL)
       
        elif -3 in self.mySums: 
            self.myLabel.config(text="Player 2 won!")
            
            for i in range(1,10):
                if self.bState[i] == 0:
                    self.bList[i].config(text="", state=DISABLED)
               
            self.gameDone = TRUE
            self.again_button.config(state=NORMAL)
          

    def do_sums(self):

        triples = [[1,2,3], [4,5,6], [7,8,9], 
                   [1,4,7], [2,5,8], [3,6,9], 
                   [1,5,9], [3,5,7]]          
        count = 0
        for i in triples:
            self.mySums[count] = 0
            for j in i:
                self.mySums[count] += self.bState[j]

            count += 1

    def do_move(self):
       
      
        if (not 1 in self.bState) and (not -1 in self.bState): 
            if random.random() < 0.20:   
                self.do_button(5)
                return

      
        if (1 in self.bState) and (not -1 in self.bState):
            if self.bState.index(1) in [1,3,7,9]:
                self.do_button(5)
                self.specialDefense = TRUE
                return

        
        for i in range(1,10):
            if self.bState[i] == 0:
                self.bState[i] = -1  
                self.do_sums()
                if -3 in self.mySums: 
                    self.do_button(i) 
                    return
                else:
                    self.bState[i] = 0 

    
        for i in range(1,10):
            if self.bState[i] == 0:
                self.bState[i] = 1   
                self.do_sums()
                if 3 in self.mySums: 
                    self.do_button(i) 
                    self.specialDefense = FALSE 
                    return
                else:
                    self.bState[i] = 0 

       
        if self.specialDefense:
            self.specialDefense = FALSE
            sides = [2,4,6,8]
            random.shuffle(sides)  
            for i in sides:
                if self.bState[i] == 0:
                    self.do_button(i)
                    return

      
        corners = [1,3,7,9]
        random.shuffle(corners)   
        for i in corners:
            if self.bState[i] == 0:
                self.do_button(i)
                return

       
        if self.bState[5] == 0:
            self.do_button(5)
            return

       
        sides = [2,4,6,8]
        random.shuffle(sides)  
        for i in sides:
            if self.bState[i] == 0:
                self.do_button(i)
                return

    def do_again(self):
       
  
        self.player1_button.config(state=NORMAL)
        self.player2_button.config(state=NORMAL)
        self.myLabel.config(text="Who starts?")

       
        for i in range(1,10):
            self.bList[i].config(text="", state=DISABLED)

    def do_exit(self):
      
        Tk.destroy(self)
        

def but1():
    if __name__ == '__main__':
        root = MyApp()
        root.title("Tic Tac Toe")
        root.geometry("600x600")

        root.configure(background="purple")
        root.mainloop()
        
b1.configure(command=but1) 


class MyApp2(Tk):
    def __init__(self):
    
     
        Tk.__init__(self)

      
        fr = Frame(self)

       
        self.player_button = Button(self, text="Me",
                                    command=lambda: self.do_start(TRUE),bg="yellow",fg="black",
                                    font=("Open Sans", 16,"bold"))
        self.computer_button = Button(self, text="Computer",
                                      command=lambda: self.do_start(FALSE),bg="yellow",fg="black",
                                    font=("Open Sans", 16,"bold"))
        self.exit_button = Button(self, text="Exit", command=self.do_exit,bg="yellow",fg="black",
                                    font=("Open Sans", 16,"bold"))
        self.again_button = Button(self, text="again?", command=self.do_again,
                                   state=DISABLED,bg="yellow",fg="black",
                                    font=("Open Sans", 16,"bold"))
        self.myLabel = Label(self, text="Who starts?", bg="black",fg="white",
                                    font=("Open Sans", 16,"bold"))

       
        self.bList = [0,1,2,3,4,5,6,7,8,9]

      
        for i in range(1,10):
            self.bList[i] = Button(self, text="",  #bList now button references
                                   command=lambda j=i: self.do_button(j),
                                   state=DISABLED, relief=RAISED, height=3,
                                   width=7, font=("Open Sans", 24))

      
        fr.grid()
        self.myLabel.grid(row=0, columnspan=4)
        self.player_button.grid(row=1, column=0)
        self.computer_button.grid(row=1, column=2)
        self.exit_button.grid(row=5, column=0)
        self.again_button.grid(row=5, column=2)

      
        myL = [[1,4,0], [2,4,1], [3,4,2],  
               [4,3,0], [5,3,1], [6,3,2],
               [7,2,0], [8,2,1], [9,2,2]]
        for i in myL:
            self.bList[i[0]].grid(row=i[1], column=i[2])

    def do_start(self,player):
      
    
        self.player_button.config(state=DISABLED)
        self.computer_button.config(state=DISABLED)
        self.again_button.config(state=DISABLED)

       
        self.bState = [10,0,0,0,0,0,0,0,0,0] 
        self.mySums = [0,0,0,0,0,0,0,0]      
        self.gameDone = FALSE
        self.specialDefense = FALSE

       
        for i in range(1,10):
            self.bList[i].config(state=NORMAL)

       
        self.myLabel.config(text="You are X, make a move")
        if player:
            self.turn = FALSE
        else:
            self.turn = TRUE
            self.do_move()

    def do_button(self, i):
  
       
        if self.turn:
            myText = "0"
            self.turn = FALSE
            self.bState[i] = -1
        else:
            myText = "X"
            self.turn = TRUE
            self.bState[i] = 1

        
        self.bList[i].config(text=myText, state=DISABLED)
        self.test_done()

       
        if (self.turn) and (not self.gameDone):
            self.do_move()
  
    def test_done(self):
       
      
        if not (0 in self.bState):
            self.myLabel.config(text="Draw!")
         
            self.again_button.config(state=NORMAL)

       
        self.do_sums()
        if 3 in self.mySums: 
            self.myLabel.config(text="You won!")
          
            for i in range(1,10):
                if self.bState[i] == 0:
                    self.bList[i].config(text="", state=DISABLED)
            self.gameDone = TRUE 
            
            self.again_button.config(state=NORMAL)
       
        elif -3 in self.mySums: 
            self.myLabel.config(text="Computer won!")
            
            for i in range(1,10):
                if self.bState[i] == 0:
                    self.bList[i].config(text="", state=DISABLED)
               
            self.gameDone = TRUE
            self.again_button.config(state=NORMAL)
          

    def do_sums(self):
        
        triples = [[1,2,3], [4,5,6], [7,8,9], 
                   [1,4,7], [2,5,8], [3,6,9], 
                   [1,5,9], [3,5,7]]          
        count = 0
        for i in triples:
            self.mySums[count] = 0
            for j in i:
                self.mySums[count] += self.bState[j]

            count += 1

    def do_move(self):
     
        
        if (not 1 in self.bState) and (not -1 in self.bState): 
            if random.random() < 0.20:  
                self.do_button(5)
                return

      
        if (1 in self.bState) and (not -1 in self.bState):
            if self.bState.index(1) in [1,3,7,9]:
                self.do_button(5)
                self.specialDefense = TRUE
                return

       
        for i in range(1,10):
            if self.bState[i] == 0:
                self.bState[i] = -1   
                self.do_sums()
                if -3 in self.mySums: 
                    self.do_button(i) 
                    return
                else:
                    self.bState[i] = 0 

        
        for i in range(1,10):
            if self.bState[i] == 0:
                self.bState[i] = 1   
                self.do_sums()
                if 3 in self.mySums: 
                    self.do_button(i) 
                    self.specialDefense = FALSE 
                    return
                else:
                    self.bState[i] = 0 

       
        if self.specialDefense:
            self.specialDefense = FALSE
            sides = [2,4,6,8]
            random.shuffle(sides)  
            for i in sides:
                if self.bState[i] == 0:
                    self.do_button(i)
                    return


        corners = [1,3,7,9]
        random.shuffle(corners)   
        for i in corners:
            if self.bState[i] == 0:
                self.do_button(i)
                return

       
        if self.bState[5] == 0:
            self.do_button(5)
            return

    
        sides = [2,4,6,8]
        random.shuffle(sides)  
        for i in sides:
            if self.bState[i] == 0:
                self.do_button(i)
                return

    def do_again(self):
      
       
        self.player_button.config(state=NORMAL)
        self.computer_button.config(state=NORMAL)
        self.myLabel.config(text="Who starts?")

        
        for i in range(1,10):
            self.bList[i].config(text="", state=DISABLED)

    def do_exit(self):
      
        Tk.destroy(self)


def but2():
    
    if __name__ == '__main__':
        root2 = MyApp2()
        root2.title("Tic Tac Toe")
        root2.geometry("600x600")
        root2.configure(background="green")
        root2.mainloop()
b2.configure(command=but2)
root1.mainloop()
