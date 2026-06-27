##BMI CALCULATOR
#INPUTS
m = float(input("Your mass in kg = "))
h = float(input("Your height in m  = "))

#CALCULATION
bmi = m/(h**2)
print("Your BMI = ",bmi)
#IDENTIFIES RANGE
if bmi<18.5:
    print("Underweight")
elif bmi<24.9:
    print("Normal")
elif bmi<29.9:
    print("Overweight")
elif bmi<30:
    print("Obese")
elif bmi<34.9:
    print("Obese Class I")
elif bmi<39.9:
    print("Obese Class II")
else:
    print("Obese Class III")

