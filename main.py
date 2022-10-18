import tkinter
from tkinter import *
from tkinter import messagebox


win = tkinter.Tk()

win.geometry("300x312")
win.resizable(0,0)
win.title("TicTacToe")
img = tkinter.PhotoImage(file = "imageedit_1_7388969709.png")
win.iconphoto(False,img)

player = "X"

end = False

def reset():
    for i in range(0, 3):
        for j in range(0, 3):
            b[i][j].config(text ="", bg="white")
            global state
            state = [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]




def clicked(r,c):

    global player

    if player == "X" and state[r][c] == 0 and end == False:
        b[r][c].config(text = "X")
        state[r][c]="X"
        player = "O"


    elif player == "O" and state[r][c] == 0 and end == False:
        b[r][c].config(text = "O")
        state[r][c]="O"
        player = "X"
    checkWin()

def checkWin():
    for i in range (0,3):
        if state[i][0] == state[i][1] == state [i][2] == "X":
            end= True
            b[i][0].config(bg="green")
            b[i][1].config(bg="green")
            b[i][2].config(bg="green")
            tkinter.messagebox.showinfo("WINNER","X WON")
            reset()
        elif state[i][0] == state[i][1] == state [i][2] == "O":
            end = True
            b[i][0].config(bg="green")
            b[i][1].config(bg="green")
            b[i][2].config(bg="green")
            tkinter.messagebox.showinfo("WINNER", "O WON")
            reset()
        elif state[0][i] == state[1][i] == state [2][i] == "X":
            end = True
            b[0][i].config(bg="green")
            b[1][i].config(bg="green")
            b[2][i].config(bg="green")
            tkinter.messagebox.showinfo("WINNER", "X WON")
            reset()
        elif state[0][i] == state[1][i] == state [2][i] == "O":
            end = True
            b[0][i].config(bg="green")
            b[1][i].config(bg="green")
            b[2][i].config(bg="green")
            tkinter.messagebox.showinfo("WINNER", "O WON")
            reset()
        elif state[0][0] == state[1][1] == state[2][2] == "X":
            end = True
            b[0][0].config(bg="green")
            b[1][1].config(bg="green")
            b[2][2].config(bg="green")
            tkinter.messagebox.showinfo("WINNER", "X WON")
            reset()
        elif state[0][0] == state[1][1] == state[2][2] == "O":
            end = True
            b[0][0].config(bg="green")
            b[1][1].config(bg="green")
            b[2][2].config(bg="green")
            tkinter.messagebox.showinfo("WINNER", "O WON")
            reset()
        elif state[0][2] == state[1][1] == state[2][0] == "X":
            end = True
            b[0][2].config(bg="green")
            b[1][1].config(bg="green")
            b[2][0].config(bg="green")
            tkinter.messagebox.showinfo("WINNER", "X WON")
            reset()
        elif state[0][2] == state[1][1] == state[2][0] == "O":
            end = True
            b[0][2].config(bg="green")
            b[1][1].config(bg="green")
            b[2][0].config(bg="green")
            tkinter.messagebox.showinfo("WINNER", "O WON")
            reset()
        elif state[0][0] and state[0][1] and state[0][2] and state[1][0] and state[1][1] and state[1][2] and state[2][0] and state[2][1] and state[2][2] != 0:
            for i in range(0, 3):
                for j in range(0, 3):
                    b[i][j].config(bg="purple")
            end = True

            tkinter.messagebox.showinfo("TIE", "It\'s a Tie")
            reset()


b=[[0,0,0],
   [0,0,0],
   [0,0,0]]

state = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range (0,3):
    for j in range (0,3):
        b[i][j]= tkinter.Button(win,text ="",font = 10 ,width = 10,height = 5, command =lambda r=i,c=j : clicked(r,c))
        b[i][j].grid(row = i, column = j)





win.mainloop()
