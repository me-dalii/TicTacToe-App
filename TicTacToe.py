from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as f

mainWindow = Tk()
mainWindow.title("tac touc")
mainWindow.geometry("800x650")


#***************************functions***********************
def raise_frame():
	mainFrame.pack_forget()
	gameFrame.pack(expand=True)
def Win(l,XO):
	win_conditions = ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))
	for w in win_conditions:
		it_test = 0
		for wiw in w:
			if wiw in l:
				it_test+=1
				if it_test==3:
					messagebox.showinfo("You Win!",XO +" Has Won")
					msg = messagebox.askquestion("Game Over", "Wanna play again?")
					if msg == "yes":
						play_again()
					else:
						mainWindow.destroy()
					break
				else:
					continue
		if it_test == 3:
			break
def play_again():
	for un in all_buttons:
		un.config(text = " ")
		X_list.clear()
		O_list.clear()

test = True
X_list = []
O_list = []
def update(b_name, b_num):
	# x = true, o = false
	global test, X_list, O_list

	if b_name["text"] == " ":
		if test == True:
			b_name.config(text = "X", fg = "blue")
			X_list.append(b_num)
			test = False
			if len(X_list) >= 3:
				Win(X_list,"X")

		else:
			b_name.config(text = "O", fg = "red")
			O_list.append(b_num)
			test = True
			if len(O_list) >= 3:
				Win(O_list,"O")
	if len(X_list + O_list) == 9:
		msg = messagebox.askquestion("Game Over", "Wanna play again?")
		if msg == "yes":
			play_again()
		else:
			mainWindow.destroy()
		
	

#***********************************************************
#***************************Main Frame***************************************
mainFrame = Frame(mainWindow)
mainFrame.pack()

Label(mainFrame, text = "Welcome To Tac Touc", font = "Helvetica 45").pack(anchor = CENTER, fill = BOTH)


Play_B = Button(mainFrame, text = "Play", font="TIMES 18", bg = "green" ,width = "250", command = raise_frame)
Play_B.pack(anchor = CENTER, fill = BOTH)


gameFrame = Frame(mainWindow)
hx,wx=1,3

myFont = f.Font(family ="TIMES", size=70, weight="bold")



b1 = Button(gameFrame, text = " ", height = hx, width = wx, command = lambda: update(b1,1))
b2 = Button(gameFrame, text = " ", height = hx, width = wx, command = lambda: update(b2,2))
b3 = Button(gameFrame, text = " ", height = hx, width = wx, command = lambda: update(b3,3))

b4 = Button(gameFrame, text = " ", height = hx, width = wx, command = lambda: update(b4,4))
b5 = Button(gameFrame, text = " ", height = hx, width = wx, command = lambda: update(b5,5))
b6 = Button(gameFrame, text = " ", height = hx, width = wx, command = lambda: update(b6,6))

b7 = Button(gameFrame, text = " ", height = hx, width = wx, command = lambda: update(b7,7))
b8 = Button(gameFrame, text = " ", height = hx, width = wx, command = lambda: update(b8,8))
b9 = Button(gameFrame, text = " ", height = hx, width = wx, command = lambda: update(b9,9))

all_buttons=(b1,b2,b3,b4,b5,b6,b7,b8,b9)

for i in all_buttons:
	i["font"] = myFont

b1.grid(row = 0, column = 0)
b2.grid(row = 0, column = 1)
b3.grid(row = 0, column = 2)

b4.grid(row = 1, column = 0)
b5.grid(row = 1, column = 1)
b6.grid(row = 1, column = 2)

b7.grid(row = 2, column = 0)
b8.grid(row = 2, column = 1)
b9.grid(row = 2, column = 2)




mainWindow.mainloop()
