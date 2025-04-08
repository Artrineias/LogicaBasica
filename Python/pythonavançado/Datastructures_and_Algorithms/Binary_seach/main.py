from random import randint

#Esse codigo tem a função de descobrir o valor sorteado pelo computador não importa
# o tamanho do valor numerico
def advivenhe_um_numero(pc,user):
    primeiro = 0
    ultimo = int(user)
    
    c = 0
    teste = 0
    while True:
        if pc == primeiro:
            print(f"Você conseguiu acerta o valor {primeiro}!!!")
            break
        else:
            meio = (primeiro+ultimo)//2
            c += 1
            print(f"{c}°Tentativa")

            #Isso serve pra que em casos de numeros como 19.5 que 
			#fazer o codigo ficar em loop
            if meio == teste:
                meio += 1
            elif meio != teste:
                teste = meio            
            #

            if pc > meio:
                primeiro = meio + 1
            elif pc < meio:
                ultimo = meio - 1
            else:
                meio

#Esse é comparação com um codigo mais simples e menos eficiente
def simples(pc,max):
    
    for i in range(0,max,1):
        if i == pc:
            print("Voce consguiu!")
            break
        else:
            print(f"{i}°tentativa")

if __name__=="__main__":
    x = 1000
    user = x 
    pc = randint(0,x)
    advivenhe_um_numero(pc,user)
    simples(pc,x)