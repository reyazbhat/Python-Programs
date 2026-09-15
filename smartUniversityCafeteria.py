print("=" * 60)

print("          SMART UNIVERSITY CAFETERIA DASHBOARD")

print("=" * 60)


# Student Information

name = input("Enter your name: ")

iD = int(input("Enter your ID: "))

category = input("Enter the category: ").lower()


# Menu

menu = {
    "biryani": 120,
    "burger": 80,
    "chicken": 150,
    "mutton": 200
}


# Food Order

foodOrder = input("Enter the food name you want to order: ").lower()

quantity = int(input("Enter the total quantity: "))


# Check Food Availability

if foodOrder in menu:
    food = True
    price = menu[foodOrder]
else:
    food = False
    price = 0


# Calculate Subtotal

if food == True:
    subtotal = price * quantity
else:
    subtotal = 0


# Student Discount

if category == "student":
    studentDiscount = subtotal * 0.10
else:
    studentDiscount = 0


# Coupon

coupon = input("Enter coupon code: ").upper()

if coupon == "SAVE20" and subtotal >= 200:
    couponValid = True
    couponDiscount = subtotal * 0.20
else:
    couponValid = False
    couponDiscount = 0


# Delivery Charge

if subtotal >= 300:
    deliveryCharge = 0
else:
    deliveryCharge = 30


# Final Amount

finalAmount = subtotal - studentDiscount - couponDiscount + deliveryCharge


# Balance

balance = float(input("Enter your available balance: ₹"))


# Check Balance

if finalAmount <= balance:
    sufficientBalance = True
else:
    sufficientBalance = False


# Order Confirmation

if food == True and sufficientBalance == True:
    orderStatus = "ORDER CONFIRMED"

    # Update Balance
    balance -= finalAmount

else:
    orderStatus = "ORDER REJECTED"


# Digital Receipt

print("\n")
print("=" * 60)

print("          SMART UNIVERSITY CAFETERIA")

print("=" * 60)

print("STUDENT INFORMATION")

print("Name     :", name)
print("ID       :", iD)
print("Category :", category.title())

print("-" * 60)

print("ORDER INFORMATION")

print("Food Item :", foodOrder.title())
print("Quantity  :", quantity)
print("Price     : ₹", price)

print("-" * 60)

print("BILL")

print("Subtotal         : ₹", subtotal)
print("Student Discount : ₹", studentDiscount)
print("Coupon Discount  : ₹", couponDiscount)
print("Delivery Charge  : ₹", deliveryCharge)

print("FINAL AMOUNT     : ₹", finalAmount)

print("-" * 60)

print("STATUS")

if food == True:
    print("Menu Item : ✓ AVAILABLE")
else:
    print("Menu Item : ✗ UNAVAILABLE")


if couponValid == True:
    print("Coupon    : ✓ VALID")
else:
    print("Coupon    : ✗ INVALID")


if sufficientBalance == True:
    print("Balance   : ✓ SUFFICIENT")
else:
    print("Balance   : ✗ INSUFFICIENT")


print("-" * 60)

print(orderStatus)

print("Remaining Balance : ₹", balance)

print("=" * 60)