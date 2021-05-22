import random
from tkinter import *
from tkinter import messagebox
computer = random.randint(1, 3)
computerChoice = ""
userChoice = ""
print(computer)


def rock():
    userChoice = "Rock"
    if userChoice == "Rock" and computerChoice == "Scissors":
        msg = messagebox.showinfo(
            "YOU WON!!😃😃😃 ", "COMPUTER CHOOSE " + computerChoice.upper())
        root.destroy()
    elif userChoice == "Rock" and computerChoice == "Rock":
        msg = messagebox.showinfo(
            "NO ONE WON!! ", "COMPUTER CHOOSE " + computerChoice.upper())
        root.destroy()
    elif userChoice == "Rock" and computerChoice == "Paper":
        msg = messagebox.showinfo(
            "YOU LOSE!!😔😔😔 ", "COMPUTER CHOOSE " + computerChoice.upper())
        root.destroy()


def paper():
    userChoice = "Paper"
    if userChoice == "Paper" and computerChoice == "Rock":
        msg = messagebox.showinfo(
            "YOU WON!!😃😃😃 ", "COMPUTER CHOOSE " + computerChoice.upper())
        root.destroy()
    elif userChoice == "Paper" and computerChoice == "Paper":
        msg = messagebox.showinfo(
            "NO ONE WON!! ", "COMPUTER CHOOSE " + computerChoice.upper())
        root.destroy()
    elif userChoice == "Paper" and computerChoice == "Scissors":
        msg = messagebox.showinfo(
            "YOU LOSE!!😔😔😔 ", "COMPUTER CHOOSE " + computerChoice.upper())
        root.destroy()


def scissors():
    userChoice = "Scissors"
    if userChoice == "Scissors" and computerChoice == "Paper":
        msg = messagebox.showinfo(
            "YOU WON!!😃😃😃 ", "COMPUTER CHOOSE " + computerChoice.upper())
        root.destroy()
    elif userChoice == "Scissors" and computerChoice == "Scissors":
        msg = messagebox.showinfo(
            "NO ONE WON!!", "COMPUTER CHOOSE " + computerChoice.upper())
        root.destroy()
    elif userChoice == "Scissors" and computerChoice == "Rock":
        msg = messagebox.showinfo(
            "YOU LOSE!!😔😔😔 ", "COMPUTER CHOOSE " + computerChoice.upper())
        root.destroy()


root = Tk()
root.geometry('425x150')
root.title("Rock Paper Scissor Game")
if computer == 1:
    computerChoice = "Rock"
elif computer == 2:
    computerChoice = "Paper"
else:
    computerChoice = "Scissors"

R = Button(root, text="ROCK", command=rock, bg='black',
           fg="white", font="TimesNewRoman", padx=10, bd=10)
P = Button(root, text="PAPER", command=paper, bg='black',
           fg="white", font="TimesNewRoman", padx=10, bd=10)
S = Button(root, text="SCISSORS", command=scissors, bg='black',
           fg="white", font="TimesNewRoman", padx=10, bd=10)
R.place(x=50, y=50)
P.place(x=150, y=50)
S.place(x=260, y=50)
root.mainloop()
