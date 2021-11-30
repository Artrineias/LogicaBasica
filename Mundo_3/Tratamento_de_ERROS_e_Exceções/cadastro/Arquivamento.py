
import prints, os.path

def arquivos (name='name',age='age'):
    if name in "name" and age in "age":
        if name == "name":
            arquivo = open(f"Mundo_3/Tratamento_de_ERROS_e_Exceções/cadastro/{name}.txt","a", newline="")    
            texto = prints.name()
            arquivo.write(texto+'\n')
            arquivo.close()
        
        if age == "age":
            arquivo = open(f"Mundo_3/Tratamento_de_ERROS_e_Exceções/cadastro/{age}.txt","a", newline="")
            texto = prints.age()
            arquivo.write(texto+'\n')
            arquivo.close()        
        

    else:
        return print("Nome de arquivo não definido")

def mostra(name="name",age="age"):

    if os.path.exists(f"Mundo_3/Tratamento_de_ERROS_e_Exceções/cadastro/{name}.txt") and os.path.exists(f"Mundo_3/Tratamento_de_ERROS_e_Exceções/cadastro/{age}.txt"):    
        text_name = list(open(f"Mundo_3/Tratamento_de_ERROS_e_Exceções/cadastro/{name}.txt","r"))
        text_age  = list(open(f"Mundo_3/Tratamento_de_ERROS_e_Exceções/cadastro/{age}.txt","r"))
        tamanho = len(text_name)
        for x in range(0,tamanho):
            n= text_name[x].strip('\n')
            i = text_age[x].strip('\n')
            print(f"{n:<15} {i:<2} anos")
    else:
        arquivos('name')
        arquivos('age')
