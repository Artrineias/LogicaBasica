import POO.manipulator as manipulator

while True:
    print("="*17+"OPÇÕES"+"="*17)
    print("1-Ver informações de um usuario.")
    print("2-Salvar um novo usuario no arquivo.")
    print("9-Finalizar o Execução.")
    print("=+"*20)
    opç = int(input("Escolha a opção:"))
    if opç == 1:
        user = input("Usuario:")
        senha = input("Senha:")
        manipulator.Busca_arqui("Dados",user,senha)
    if opç == 2:
        obj = manipulator.obj_usuario()
        manipulator.set_Usuario_arquivos("Dados",obj)
    if opç == 9:
        break
