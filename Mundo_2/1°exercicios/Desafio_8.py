weight = float(input('Enter the wright:(kg)'))
height = float(input('Enter the height:(m)'))
imc = weight/(height*height)
print('your BMI is in {}'.format
      (imc))
if imc < 18.5:
    print('You are Low Wight')
elif imc >= 18.5 and imc < 24.9:
    print('You are Normal Weight')
elif imc >= 25 and imc < 29.9:
    print('You are Overweight')
elif imc >= 30 and imc < 34.9:
    print('You are Obesity')
elif imc >= 35 and imc < 39.9:
    print('You are Severe Obesity')
else:
    print('You are Morbid Obesity')
