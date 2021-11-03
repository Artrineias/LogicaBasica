def area(largura,comprimento):
    area =comprimento * largura
    print(area)

c = float(input("width:"))
l = float(input("length:"))
print(f"The area of ​​a {c} X {l} plot is",end=" ")
area(c,l)