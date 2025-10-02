w=float(input("Give me your weight in pounds "))
h=float(input("Give me your height in inches "))
bmi=703*w/(h*h)
print("Your bmi is ",bmi)
if bmi<18.5:
    print("Underweight")
elif 18.5<bmi<24.9:
    print("Normal")
elif 25<bmi<29.9:
    print("Overwieght")
else:
    print("Obese")
