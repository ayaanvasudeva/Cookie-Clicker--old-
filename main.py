from tkinter import *
from PIL import Image,ImageTk
from art import nintendo

root = Tk()
root.geometry("700x700")
root.configure(background = 'yellow')

Money = 0
salary = 10
space ="                                                                                                                           "
def a():
  global Money
  global salary
  if Money >= 1000:
    global space
    Money -= 1000
    salary += 30
    remove_label2232 = Label(root, text = space, bg = 'yellow').grid(row  = 9, column = 1)
  else:
     global laabel1212
     hello123 = Label(root, text = space, bg = 'yellow').grid(row = 9, column = 1)
     laabel1212 = Label(root, text = "You don't have enough Cookies to invest in apple", bg = 'yellow').grid(row = 9, column = 1)
    
def Enter():
  get = Label(root, text = code.get() )
  get.grid(row = 4, column = 2)
def badges():
  global code
  t = Label(root, text = space, bg = 'yellow').grid(row = 1, column = 2)
  t1 = Label(root, text = space, bg = 'yellow').grid(row = 2, column = 2)
  t2 = Label(root, text = space, bg = 'yellow').grid(row = 3, column = 2)
  code = Entry(root).grid(row = 1, column = 2)
  enter = Button(root, text = "Enter", command = Enter).grid(row = 2, column = 2)
  info = Label(root, text = "^Type the code above^").grid(row = 3, column = 2)
def rules():
  instructions = Label(root,text = "You will need 2+ players and 2+ devices.").grid(row = 1, column = 2)
  goal2 = Label(root, text = "Goal: Be the first player to reach 1,000,000,000 (1 billion) Cookies.").grid(row = 2, column = 2)
  goal1 = Label(root, text = "When reached 1 billion Cookies press finish").grid(row = 3, column = 2)
def money():
  global Money
  global salary
  Money += salary
  hi = Label(root, text = space, bg = 'yellow').grid(row = 1, column = 2)
  hi2 = Label(root, text = space, bg = 'yellow').grid(row = 2 , column = 2)
  hi3 = Label(root, text = space, bg = 'yellow').grid(row = 3, column = 2)
  cool_animation = Label(root, text = f"+ {salary} Cookies", bg = 'yellow').grid(row = 3, column = 0)
def show():
  a1 = Label(root, text = space, bg = 'yellow').grid(row = 8 ,column = 1)
  label = Label(root, text = f"{Money} Cookies   ", bg = 'yellow').grid(row = 8, column = 1)
def Switch():
  global Money
  global salary
  if Money >= 100:
    global space
    Money -= 100
    salary += 5
    remove_label = Label(root, text = space, bg = 'yellow').grid(row  = 9, column = 1)
  
  else:
    global laabel
    laabel = Label(root, text = "You don't have enough Cookies to invest in nintendo", bg = 'yellow').grid(row = 9, column = 1)
  

def winner():
  global Money
  if Money >= 1000000000:
    yay = Label(root, text = "You win").grid(row = 10, column = 1)
  else:
    cheat = Label(root, text = "You do not have enough Cookies", bg = 'yellow').grid(row = 10, column = 1)
    
root.title("Cookie clicker (By Ayaan V.)")
img1 = ImageTk.PhotoImage(Image.open("cookie.jpeg"))
mylabel = Button(image = img1, command = money, padx = 30, pady = 30)
mylabel.grid(row = 3, column = 1)
img2 = ImageTk.PhotoImage(Image.open("nin2.png"))
mylabel1 = Button(image = img2, command = Switch, padx = 20, pady = 20)
mylabel1.grid(row = 5, column = 1)


Cookie = Label(root, text = "Cookie clicker", fg = 'white', bg = 'black', font = ("helvetica", 50)).grid(row = 0, column = 1)
Badge = Button(root, text = "Badges", bg = "lightblue", command = badges).grid(row = 1, column = 1)
game_rules = Button(root, text = "Game rules", bg = "lightblue", command = rules).grid(row = 2, column = 1)


show_money = Button(root, text = "Show Cookies", bg = "lightblue", command = show).grid(row = 4, column = 1)

apple = Button(root, text = " Invest $1000 in apple", bg = "red", fg = "black", command = a).grid(row = 6, column = 1)
finish = Button(root, text = "Finish",fg = "white", bg = "black", command = winner).grid(row = 7, column = 1)
root.mainloop()
