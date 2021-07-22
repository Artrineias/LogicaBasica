weight = float(input('Enter the wright:'))
height = float(input('Enter the height:'))
imc = weight/(height*height)
if imc < 18.5:
    print('Low Wight')
elif imc >= 18.5 and imc < 24.9:
    print('Normal Weight')
elif imc >= 25 and imc < 29.9:
    print('Overweight')
elif imc >= 30 and imc < 34.9:
    print('Obesity')
elif imc >= 35 and imc < 39.9:
    print('Severe Obesity')
else:
    print('Morbid Obesity')
