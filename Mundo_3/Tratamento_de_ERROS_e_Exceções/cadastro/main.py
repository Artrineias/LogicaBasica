import prints,Arquivamento
while True:
    prints.traço(30)
    prints.formatador("MENU PRINCIPAL")
    prints.traço(30)
    print("""
    1- Ver pessoas cadastradas.
    2- Cadastra nova Pessoa.
    3- Sair do Sistema
    """)
    prints.traço(30)
    chamada=input("Sua Opção: ")
    prints.traço(30)
    verificador = prints.verificaçãoage(chamada)
    if chamada == '1':
        Arquivamento.mostra()
    elif chamada == '2':
        Arquivamento.arquivos()
    elif chamada == '3':
        break
    else:
        prints.formatador("Erro, Digite uma das opções.")
    

