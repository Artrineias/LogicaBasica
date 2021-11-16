c = [   '\033[m' #Padrão
        '\033[0;0m'# restara
        '\033[1;40m', #Preto  
        '\033[1;41m', #Vermelho 
        '\033[1;42m', #Verde 
        '\033[1;43m', #Amarelo 
        '\033[1;44m', #Azul 
        '\033[1;45m', #Magenta 
        '\033[1;46m', #Cyan 	 	    
 		'\033[1;47m', #Cinza Claro

]


def ajuda (com):
    help(com)


def titulo (text,cor=0):
    tam =len(text) + 4
    print('~'*tam)  
    print(f"  {text}  ")
    print('~'*tam)

#main

titulo("Função do Python --> ")
