def verifier(num):  
    mai = num[0]  
    for x in num:
        if mai < x:
            mai = x
    return mai


def maior(*num):
    if num != ():
        for x in num:
            print(x,end=" ")
        print(f"{len(num)} values ​​were given in total.")
        print(f"The highest value entered was {verifier(num)}")
    else:
        print(f"0 values ​​were informed in total.")
        print(f"The highest value informed was 0")


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