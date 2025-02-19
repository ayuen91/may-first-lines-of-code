height = float(input('what is your height in metres?'))
mass = float(input('what is your weight in kg?'))
 
bmi = mass / height ** 2

print('You are', 'underweight' if bmi < 18.5 else 'overweight' if bmi > 25 else 'healthy')    
print(f'Your BMI is {bmi:.2f}')