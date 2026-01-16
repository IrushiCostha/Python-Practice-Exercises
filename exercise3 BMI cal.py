print('Welcome to the BMI Calculator!')
w = int(input('Enter your weight in kg: '))
h = float(input('Enter your height in m: '))
BMI = w/h**2

if BMI < 18.5:
    print(f'Your BMI is {BMI}, You are underweighted! ')
elif 18.5< BMI <25:
    print(f'Your BMI is {BMI}, You have normal weight! ')
elif 25< BMI <30:
    print(f'Your BMI is {BMI}, You are slightly overweight! ')
elif 30< BMI <35:
    print(f'Your BMI is {BMI}, You are obese! ')
else:
    print(f'Your BMI is {BMI}, You are clinically obese! ')
