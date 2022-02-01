from re import U
from usuario import usuario

def Busca_arqui(arqui,name,senha):
    
    with open(f"POO/{arqui}.txt","r+") as j:
        a = j.readlines()
        x = len(a)
        for i in range(0,x,1):    
            b = a[i].split(';')
            if b[0] == name: 
                nome = usuario(b[0],b[1],b[2],b[3])
                if usuario.verificador(b[2],senha):
                    return True

def Busca_usuario(arqui,name,senha,informação):
    with open(f"POO/{arqui}.txt","r+") as j:
        a = j.readlines()
        x = len(a)
        for i in range(0,x,1):    
            b = a[i].split(';')
            if b[0] == name: 
                nome = usuario(b[0],b[1],b[2],b[3])
                if usuario.verificador(b[2],senha):
                    if informação == 0:
                        return nome.name,nome.idade,nome.saldo
                    elif informação == 1:
                        return nome.name
                    elif informação == 2:
                        return nome.idade
                    elif informação == 3:
                        return nome.saldo
                    elif informação == 4:
                        return nome.senha



def Alterar_dados(Obj):
    pass


def obj_usuario():
    name = str(input("Nome: "))
    idade = int(input("Idade: "))
    senha = str(input("Senha: "))
    saldo = int(input("Saldo: "))
    user = usuario(name,idade,senha,saldo)
    return user


def set_Usuario_arquivos(name,obj):
    with open(f"POO/{name}.txt","a+") as arqui:
        arqui.writelines(str(obj.name))
        arqui.writelines(";")
        arqui.writelines(str(obj.idade))
        arqui.writelines(";")
        arqui.writelines(str(obj.senha))
        arqui.writelines(";")
        arqui.writelines(str(obj.saldo))