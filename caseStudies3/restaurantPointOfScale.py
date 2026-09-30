# Task 1: Item List

items = {
    101: {
        "item": "Burger",
        "price": 2.00
    },

    102: {
        "item": "Pizza",
        "price": 5.00
    },

    103: {
        "item": "Coffee",
        "price": 3.00
    }
}


# ==================================================
# Task 2: Collect Customer Orders
# ==================================================

def takeOrder(items):

    orderList = []

    while True:

        print("\n========== MENU ==========")

        for itemId, itemDetails in items.items():

            print(
                itemId,
                "-",
                itemDetails["item"],
                "$",
                itemDetails["price"]
            )

        print("0 - Finish Order")

        itemId = int(input("\nEnter Item Code: "))

        if itemId == 0:
            break

        if itemId in items:

            quantity = int(input("Enter Quantity: "))

            itemName = items[itemId]["item"]
            itemPrice = items[itemId]["price"]

            itemTotal = itemPrice * quantity

            orderList.append(
                (itemName, quantity, itemTotal)
            )

            print("Item added successfully.")

        else:

            print("Invalid Item Code.")

    return orderList


# ==================================================
# Task 3: Calculate Bill
# ==================================================

def calculateBill(orderList):

    subtotal = 0

    for order in orderList:

        subtotal += order[2]

    tax = subtotal * 0.08

    if subtotal > 50:

        discount = 5

    else:

        discount = 0

    finalTotal = subtotal + tax - discount

    return subtotal, tax, discount, finalTotal


# ==================================================
# Task 4 & Task 5: Print Receipt
# ==================================================

def printReceipt(orderList, subtotal, tax, discount, finalTotal):

    print("\n")

    print("=" * 60)

    print("             RESTAURANT RECEIPT")

    print("=" * 60)

    print(
        f"{'Item':<25}"
        f"{'Qty':<8}"
        f"{'Total':>10}"
    )

    print("-" * 60)

    for order in orderList:

        itemName = order[0].title()
        quantity = order[1]
        itemTotal = order[2]

        print(
            f"{itemName:<25}"
            f"{quantity:<8}"
            f"${itemTotal:>9.2f}"
        )

    print("-" * 60)

    print(f"{'Subtotal':<43} ${subtotal:>9.2f}")
    print(f"{'Tax (8%)':<43} ${tax:>9.2f}")
    print(f"{'Discount':<43} ${discount:>9.2f}")

    print("-" * 60)

    print(f"{'Final Total':<43} ${finalTotal:>9.2f}")

    print("=" * 60)

    print("          THANK YOU! VISIT AGAIN")

    print("=" * 60)


# ==================================================
# Main Program
# ==================================================

orderList = takeOrder(items)

subtotal, tax, discount, finalTotal = calculateBill(orderList)

printReceipt(
    orderList,
    subtotal,
    tax,
    discount,
    finalTotal
)