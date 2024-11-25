height = float(input('Enter height: '))
weight = int(input('Enter weight: '))

bmi = (weight / (height ** 2))
print(round(bmi,2))

if bmi < 18.5:
    print("Your BMI is " + str((round(bmi,2))) + ", you are underweight")
elif bmi < 25:
    print("Your BMI is " + str((round(bmi,2))) + ", you are normal weight")
elif bmi < 30:
    print(" Your BMI is " + str((round(bmi,2))) + ", you are slightly overweight")
elif bmi < 35:
    print("Your BMI is " + str((round(bmi,2))) + ", you are obese")
else:
    print("Your BMI is " + str((round(bmi,2))) + ", ritically obese, your health is at risk.")