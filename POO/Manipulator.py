from re import U
from usuario import usuario

def Busca_arqui(name,obj):
    
    with open(f"POO/{name}.txt","r+") as arqui:
        a = arqui.readlines()
        x = len(a)
        for i in range(0,x,1):    
            b = a[i].split(';')
            if b[0] == obj: 
                nome = usuario(b[0],b[1],b[2],b[3])
                if usuario.verificador(b[2]):
                    return print(f"Nome:{nome.name}\nIdade:{nome.idade}"
                    f"\nSaldo:{nome.saldo}")

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