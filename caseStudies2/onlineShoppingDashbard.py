print("ONLINE SHOPPING DASHBOARD")

product1 = input("Enter the Product 1 Name: ")
quantity = float(input("Enter the total quantity: "))
price = float(input("Enter the price: "))
subtotal = price * quantity

print("Subtotal for", product1, "is:", subtotal)


product2 = input("Enter the Product 2 Name: ")
quantity2 = float(input("Enter the total quantity: "))
price2 = float(input("Enter the price: "))
subtotal2 = price2 * quantity2

print("Subtotal for", product2, "is:", subtotal2)


product3 = input("Enter the Product 3 Name: ")
quantity3 = float(input("Enter the total quantity: "))
price3 = float(input("Enter the price: "))
subtotal3 = price3 * quantity3

print("Subtotal for", product3, "is:", subtotal3)


product4 = input("Enter the Product 4 Name: ")
quantity4 = float(input("Enter the total quantity: "))
price4 = float(input("Enter the price: "))
subtotal4 = price4 * quantity4

print("Subtotal for", product4, "is:", subtotal4)


product5 = input("Enter the Product 5 Name: ")
quantity5 = float(input("Enter the total quantity: "))
price5 = float(input("Enter the price: "))
subtotal5 = price5 * quantity5

print("Subtotal for", product5, "is:", subtotal5)


totalAmount = subtotal + subtotal2 + subtotal3 + subtotal4 + subtotal5

discount = 0
finalAmount = totalAmount

if totalAmount >= 5000:
    discount = totalAmount * 0.10
    finalAmount = totalAmount - discount


couponcode = input("Enter the coupon code in Capital letters: ")
coupon = "WELCOME"

if couponcode == coupon:
    print("Your Total Amount: ", totalAmount)
    print("Your Discounted Amount is:", finalAmount)
    print("The Total Discount is:", discount)
else:
    print("Your coupon is invalid")
    print("Your Total Amount is:", totalAmount)