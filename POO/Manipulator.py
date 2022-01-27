from re import U
from usuario import usuario

def Busca_arqui(name,obj):
    
    for i in range(0,4,1):
        with open(f"{name}.txt","r+") as arqui:
            a = arqui.readlines()
            b = a[0].split(';')
            if b[0] == obj: 
                nome = usuario(b[0],b[1],b[2],b[3])
                v = usuario.verificador(b[2])
                if v:
                    return print(f"Nome:{nome.name}\nIdade:{nome.idade}\nSaldo:{nome.saldo}")



def set_Usuario_arquivos(name,obj):
    for i in range(0,3,1):
        with open(f"{name}.txt","a+") as arqui:
            arqui.writelines(str(obj.name))
            arqui.writelines(str(obj.idade))
            arqui.writelines(str(obj.senha))
            arqui.writelines(str(obj.saldo))