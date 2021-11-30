import prints,Arquivamento,time,os
verificador = True
while True:
    if verificador:    
        prints.traço(30)
        prints.formatador("MENU PRINCIPAL")
        prints.traço(30)
    print("""
\033[0;33m1-\033[m \033[0;34mVer pessoas cadastradas\033[m.
\033[0;33m2-\033[m \033[0;34mCadastra nova Pessoa\033[m.
\033[0;33m3-\033[m \033[0;34mSair do Sistema\033[m
    """)
    prints.traço(30)
    chamada=input("\033[0;33mSua Opção: \033[m")
    prints.traço(30)
    time.sleep(0.5)
    os.system("clear")
    verificador = prints.verificaçãoage(chamada)
    if verificador:
        if chamada == '1':
            prints.traço(30)
            prints.formatador("PESSOAS CADASTRADAS")
            prints.traço(30)
            Arquivamento.mostra()
            time.sleep(1.5)
        elif chamada == '2':
            Arquivamento.arquivos()
        elif chamada == '3':
            break
        else:
            prints.formatador("\033[0;31mErro, Digite uma das opções.\033[m")

    else:
        prints.formatador("\033[0;31mErro, Digite uma das opções.\033[m")

