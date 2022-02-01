
from tkinter import *
import manipulator

def login():
    tela = Tk() 
    tela.title("Login")
    #definição geometrica
    tela.geometry("250x150")
    #usuario    
    usuario = Label(tela,
    font="arial 12",
    width= 7,
    text="Usuario")
    usuario.place(x=10,y=10)
    ent_usuario = Entry(tela)
    ent_usuario.place(x=75,y=10)
    #senha
    senha = Label(tela,
    font="arial 12",
    width= 7,
    text="Senha",
    ).place(x=6,y=40)

    ent_senha = Entry(tela,show="*")
    ent_senha.place(x=75,y=40)


    

    #botão
    entrar = Button(tela, 
    text="Entrar",
    font="arial 12",
    width= 6,
    bd = 1,
    anchor=CENTER,
    relief= "raised",
    command = lambda :botão_click())
    entrar.place(x=160,y=80)

    mostra = Label(tela,
    text="Informação",
    font="arial 12",
    width=15,
    bd=1,
    anchor=W,
    relief="solid")
    mostra.place(x=10,y=70 )
    
    def botão_click():
        name = manipulator.Busca_usuario("Dados",ent_usuario.get(),ent_senha.get(),1)
        idade = manipulator.Busca_usuario("Dados",ent_usuario.get(),ent_senha.get(),2)
        saldo = manipulator.Busca_usuario("Dados",ent_usuario.get(),ent_senha.get(),3)
        mostra["text"] = (f"Nome:{name}\nIdade:{idade}\nSaldo:{saldo}")

    tela.mainloop()



login()