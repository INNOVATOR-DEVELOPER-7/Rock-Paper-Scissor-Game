# Import Required Library
from tkinter import *
import random

# Create Object
root = Tk()

# Set geometry
root.geometry("400x400")
root.config(bg="coral")
root.resizable(0,0)

# Set title
root.title("Rock Paper Scissor Game")

# Computer Value
computer_value = {
 "0": "Rock",
 "1": "Paper",
 "2": "Scissor"
}

# Reset The Game
def reset_game():
 b1["state"] = "active"
 b2["state"] = "active"
 b3["state"] = "active"
 l1.config(text="Player    ")
 l3.config(text="Computer")
 l4.config(text="")

# Disable the Button
def button_disable():
 b1["state"] = "disable"
 b2["state"] = "disable"
 b3["state"] = "disable"

# If player selected rock
def isrock():
 c_v = computer_value[str(random.randint(0, 2))]
 if c_v == "Rock":
  match_result = "Match Draw"
 elif c_v == "Scissor":
  match_result = "Player Win"
 else:
  match_result = "Computer Win"
 l4.config(text=match_result)
 l1.config(text="Rock")
 l3.config(text=c_v)
 button_disable()

# If player selected paper
def ispaper():
 c_v = computer_value[str(random.randint(0, 2))]
 if c_v == "Paper":
  match_result = "Match Draw"
 elif c_v == "Scissor":
  match_result = "Computer Win"
 else:
  match_result = "Player Win"
 l4.config(text=match_result)
 l1.config(text="Paper")
 l3.config(text=c_v)
 button_disable()

# If player selected scissor
def isscissor():
 c_v = computer_value[str(random.randint(0, 2))]
 if c_v == "Rock":
  match_result = "Computer Win"
 elif c_v == "Scissor":
  match_result = "Match Draw"
 else:
  match_result = "Player Win"
 l4.config(text=match_result)
 l1.config(text="Scissor")
 l3.config(text=c_v)
 button_disable()

# Add Labels, roots and Button
Label(root,text="Rock Paper Scissor",font=('Britannic Bold',25,'bold'),bg="coral",fg="blue").pack(pady=20)


l1 = Label(root,text="Player ",font=("Impact",25),bg = "coral")
l1.place(x= 45, y= 75)

l2 = Label(root,text="VS",font="Arial 25 bold",bg="red")
l2.place(x = 160,y= 78)

l3 = Label(root, text="Computer", font = ("Impact",25),bg= "coral")
l3.place(x= 225, y= 75)

l4 = Label(root,text="",font="Calbri 30 bold",bg="white",width=15,borderwidth=2,relief="solid")
l4.place(x= 20, y= 140)

b1 = Button(root, text="Rock",font=('Century Gothic',18), width=7,command=isrock)
b1.place(x= 10, y= 200)

b2 = Button(root, text="Paper ",font=('Century Gothic',18), width=7,command=ispaper)
b2.place(x=140,y= 200)

b3 = Button(root, text="Scissor",font=('Century Gothic',18), width=7,command=isscissor)
b3.place(x=270,y=200)

B4= Button(root, text="Reset Game",font=("Impact",25), fg="red",bg="black", command=reset_game)
B4.place(x= 110,y= 270)

# Execute Tkinter
root.mainloop()