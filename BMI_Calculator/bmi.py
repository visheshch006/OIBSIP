print("===== BMI Calculator =====")

name = input("Enter your name: ")
weight = float(input("Enter your weight in kg: "))

feet = int(input("Enter your height (feet): "))
inch = int(input("Enter your height (inches): "))

height_meter = (feet * 0.3048) + (inch * 0.0254)

bmi = weight / (height_meter ** 2)

print("\nHello,", name)
print("Your BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal Weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")

print("\nThank you for using the BMI Calculator!")