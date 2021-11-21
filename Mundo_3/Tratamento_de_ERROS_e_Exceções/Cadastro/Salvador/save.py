import Cadastro.Leitor.prints
arquivo = open("contatos.txt", "a")
texto = arquivo.readlines()
texto.append(Cadastro.Leitor.prints.name(""))