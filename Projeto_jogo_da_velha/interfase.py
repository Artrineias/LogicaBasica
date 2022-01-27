from tkinter import *

class Application:
    def __init__(self, master=None):
      root.title("jogo da velha")
      self.primero = Button(text="1",command= x).grid(row=0,column=0)
      self.segundo = Button(text="2").grid(row=0,column=1)
      self.terceiro = Button(text="3").grid(row=0,column=2)
      self.quarto = Button(text="4").grid(row=1,column=0)
      self.quinto = Button(text="5").grid(row=1,column=1)
      self.sexto = Button(text="6").grid(row=1,column=2)
      self.setimo = Button(text="7").grid(row=2,column=0)
      self.oitavo = Button(text="8").grid(row=2,column=1)
      self.nono = Button(text="9").grid(row=2,column=2)      
def x ():
  print("X")

root= Tk()
root.geometry("110x90")
Application(root)
root.mainloop()