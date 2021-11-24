import prints

def arquivos (mgs='none'):
    if mgs in "name" or mgs in "age":
        arquivo = open(f"Mundo_3/Tratamento_de_ERROS_e_Exceções/cadastro/{mgs}.txt","a", newline="")
        if mgs == "name":    
            texto = prints.name()
        elif mgs == "age":
            texto = prints.age()
        
        arquivo.write(texto+'\n')
        arquivo.close()

    else:
        return print("Nome de arquivo não definido")

def mostra(mgs="none"):
    if mgs in "name" or mgs in "age":
        arquivo = open(f"Mundo_3/Tratamento_de_ERROS_e_Exceções/cadastro/{mgs}.txt","a", newline="")
        if mgs == "name":    
            texto = prints.name()
        elif mgs == "age":
            texto = prints.age()
        
        arquivo.write(texto+'\n')
        arquivo.close()

    else:
        return print("Nome de arquivo não definido")