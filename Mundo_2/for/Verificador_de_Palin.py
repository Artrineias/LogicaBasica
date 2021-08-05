
frase = input("digite uma frase:").strip().upper()
junto = frase.replace(" ","")
inversa = ""
for letra in range(len(junto)-1,-1,-1):
    inversa += junto[letra]
print("A Inversa da {} é {}".format(junto,inversa))
if junto == inversa:
    print("Temos um Palindromo!")
else:
    print("Não é Palindromo")
