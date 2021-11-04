def maio(num):  
    mai = num[0]  
    for x in num:
        if mai < x:
            mai = x
    return mai


def maior(*num):
    for x in num:
        print(x,end=" ")
    print(f"Foram informado {len(num)} valores ao todo.")
    print(f"O maior valor informado foi {maio(num)}")



maior(2,3,4,2,6,7,2,9)