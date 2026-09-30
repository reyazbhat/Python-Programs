# Case Study 4: Banking ATM & Transaction Ledger


# Task 1: Initialize account details

account = {
    "account_number": "88291039",
    "holder_name": "Reyaz Bhat",
    "pin": "1234",
    "balance": 1000.00,
    "transactions": []
}


# Task 2: PIN Authentication

while True:

    entered_pin = input("Enter your PIN: ")

    if entered_pin == account["pin"]:
        print("\nPIN verified successfully!")
        break

    else:
        print("Incorrect PIN. Please try again.")


# Task 3: Deposit and Withdrawal Operations

while True:

    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Check Balance
    if choice == "1":

        print("\nCurrent Balance: $", account["balance"])


    # Deposit
    elif choice == "2":

        amount = float(input("Enter deposit amount: $"))

        if amount > 0:

            account["balance"] += amount

            account["transactions"].append(
                ("Deposit", amount)
            )

            print("Deposit successful!")
            print("New Balance: $", account["balance"])

        else:

            print("Invalid deposit amount.")


    # Withdrawal
    elif choice == "3":

        amount = float(input("Enter withdrawal amount: $"))

        # Task 4: Validate withdrawal
        if amount > 0 and amount <= account["balance"]:

            account["balance"] -= amount

            account["transactions"].append(
                ("Withdrawal", amount)
            )

            print("Withdrawal successful!")
            print("New Balance: $", account["balance"])

        else:

            print("Insufficient balance or invalid amount.")


    # Exit
    elif choice == "4":

        print("\nThank you for using the ATM.")
        break


    else:

        print("Invalid choice. Please try again.")


# Task 5: Bank Account Statement Report

print("\n")
print("=" * 50)
print("             BANK STATEMENT REPORT")
print("=" * 50)

print("Account Number :", account["account_number"])
print("Holder Name    :", account["holder_name"])

print("-" * 50)

print(
    f"{'Type':<18} | "
    f"{'Amount ($)':<12} | "
    f"{'Balance ($)':<12}"
)

print("-" * 50)


# Initial balance

initial_balance = 1000.00
running_balance = initial_balance

print(
    f"{'Initial Balance':<18} | "
    f"{'---':<12} | "
    f"{running_balance:>10.2f}"
)


# Display transactions

for transaction_type, amount in account["transactions"]:

    if transaction_type == "Deposit":

        running_balance += amount

    elif transaction_type == "Withdrawal":

        running_balance -= amount

    print(
        f"{transaction_type:<18} | "
        f"{amount:>10.2f}   | "
        f"{running_balance:>10.2f}"
    )


print("-" * 50)
print(f"Closing Balance : ${account['balance']:.2f}")
print("=" * 50)