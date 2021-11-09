def verificador(num):  
    mai = num[0]  
    for x in num:
        if mai < x:
            mai = x
    return mai


def maior(*num):
    if num != ():
        for x in num:
            print(x,end=" ")
        print(f"Foram informado {len(num)} valores ao todo.")
        print(f"O maior valor informado foi {verificador(num)}")
    else:
        print(f"Foram informado 0 valores ao todo.")
        print(f"O maior valor informado foi 0")


def espaço():
    print("-="*30)

espaço()
maior(2,9,4,5,7,1)
espaço()
maior(4,7,0)
espaço()
maior(1,2)
espaço()
maior(6)
espaço()
maior()
espaço()