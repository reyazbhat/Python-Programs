# Task 1: Nested Dictionary

inventory = {
    101: {
        "name": "Laptop",
        "price": 10000,
        "stock": 17
    },
    102: {
        "name": "Iphone 17",
        "price": 150000,
        "stock": 8
    },
    103: {
        "name": "Google Pixel",
        "price": 100000,
        "stock": 15
    }
}


# Task 2: Low Stock

def lowStock(inventory):

    for product_id, details in inventory.items():

        if details["stock"] < 10:
            print(
                "Product ID:", product_id,
                "| Name:", details["name"],
                "| Stock:", details["stock"]
            )


# Task 3: Customer Purchase

def customerPurchase(inventory):

    productId = int(input("Enter the Product ID: "))
    quantity = int(input("Enter the Quantity: "))

    if productId in inventory:

        if quantity > 0 and quantity <= inventory[productId]["stock"]:

            inventory[productId]["stock"] -= quantity

            print("\nPurchase Successful")
            print("Remaining Stock:", inventory[productId]["stock"])

        else:
            print("\nInsufficient stock")

    else:
        print("Product ID not found")


# Task 4: Inventory Valuation

def calculateTotalValue(inventory):

    total = 0

    for product_id, details in inventory.items():

        total += details["price"] * details["stock"]

    return total

# Task 5: Stock Management Dashboard
def display_dashboard(inventory):

    print("\n")
    print("=" * 60)
    print("             STOCK MANAGEMENT DASHBOARD")
    print("=" * 60)

    print(f"{'ID':<8}{'Product':<20}{'Price':<12}{'Stock':<10}{'Value':<12}")
    print("-" * 60)

    for product_id, details in inventory.items():

        value = details["price"] * details["stock"]

        print(
            f"{product_id:<8}"
            f"{details['name']:<20}"
            f"₹{details['price']:<11}"
            f"{details['stock']:<10}"
            f"₹{value:<11}"
        )

    print("-" * 60)

    total_value = calculateTotalValue(inventory)

    print(f"Total Inventory Value: ₹{total_value}")
    print("=" * 60)

customerPurchase(inventory)
display_dashboard(inventory)