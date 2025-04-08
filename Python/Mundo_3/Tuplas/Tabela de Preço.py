lista = ('Lapís',1.75,'Borracha',2.0,'Caderno',15.9,
'Estojo',25.0,'Transferido',4.2,'Compasso',9.99,'Mochila'
,120.32,'Canetas',22.3,'livro',34.9)


for count in range(0,17,2):
    print(f'{lista[count]:.<30}',end =" ")
    print(f'R${lista[count+1]:>7.2f}')