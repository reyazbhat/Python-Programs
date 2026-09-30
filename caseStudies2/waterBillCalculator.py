consumer_name = input("Enter your name: ")
total_water_units = float(input("Enter the total water units consumed: "))
rate_per_unit = float(input("Enter rater per unit: "))

water_bill = total_water_units * rate_per_unit

print(consumer_name, "your total water bill is: ", water_bill)