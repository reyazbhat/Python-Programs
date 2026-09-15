person_name = input("Enter your name: ")

weight = float(input("Enter your weight in KG: "))

height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

print(person_name, "your BMI is", round(bmi, 2))