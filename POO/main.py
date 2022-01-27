import Manipulator

while True:
    print("=+"*20)
    print("===OPÇÕES===")
    print("1-Ver informações de um usuario.")
    print("2-Salvar um novo usuario no arquivo.")
    print("9-Finalizar o Execução.")
    print("=+"*20)
    opç = int(input("Escolha a opção:"))
    if opç == 1:
        user = input("O nome do usuario: ")
        Manipulator.Busca_arqui("Dados",user)
    if opç == 2:
        obj = Manipulator.obj_usuario()
        Manipulator.set_Usuario_arquivos("Dados",obj)
    if opç == 9:
        break
