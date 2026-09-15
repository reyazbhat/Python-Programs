print("=" * 60)
print("Smart University Cafeteria Dashboard")
print("=" * 60)

name = input("Enter your name")
iD = int(input("Enter your id"))
category = input("Enter the category")

menu{
    "biryani",
    "burger",
    "chawal",
    "dal"
}

def orderFood(name):
    foodOrder = input("Enter the food you want order")
    if foodOrder in menu:
        
        