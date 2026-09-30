# Case Study 7: Movie Theater Seat Reservation Engine


# ==================================================
# Task 1: Seat Matrix
# ==================================================

seatMatrix = [
    [False, False, False, False],
    [False, False, False, False],
    [False, False, False, False]
]


# ==================================================
# Task 2: Book a Seat
# ==================================================

def bookSeat(seatMatrix):

    row = int(input("Enter Row Number (0-2): "))
    column = int(input("Enter Column Number (0-3): "))

    if row >= 0 and row < 3 and column >= 0 and column < 4:

        if seatMatrix[row][column] == False:

            seatMatrix[row][column] = True

            print("Seat booked successfully.")

        else:

            print("Seat is already booked.")

    else:

        print("Invalid row or column.")

    
# ==================================================
# Task 3: Calculate Seat Statistics
# ==================================================

def calculateStatistics(seatMatrix):

    totalSeats = 0
    bookedSeats = 0

    for row in seatMatrix:

        for seat in row:

            totalSeats += 1

            if seat == True:

                bookedSeats += 1

    occupancyRate = (bookedSeats / totalSeats) * 100

    return totalSeats, bookedSeats, occupancyRate


# ==================================================
# Task 5: Display Theater Dashboard
# ==================================================

def displayDashboard(seatMatrix):

    totalSeats, bookedSeats, occupancyRate = calculateStatistics(seatMatrix)

    print("\n")
    print("=" * 50)

    print("           THEATER OCCUPANCY DASHBOARD")

    print("=" * 50)

    print("Grid Layout ([ ] = Empty, [X] = Booked):")

    for rowNumber in range(len(seatMatrix)):

        print(f"Row {rowNumber}: ", end="")

        for seat in seatMatrix[rowNumber]:

            if seat == True:

                print("[X]", end="  ")

            else:

                print("[ ]", end="  ")

        print()

    print("-" * 50)

    print(f"Total Seats     : {totalSeats}")
    print(f"Booked Seats    : {bookedSeats}")
    print(f"Occupancy Rate  : {occupancyRate:.1f}%")

    print("=" * 50)


# ==================================================
# Task 4: Interactive Menu
# ==================================================

while True:

    print("\n========== THEATER MENU ==========")
    print("1. Book Seat")
    print("2. View Theater Map")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        bookSeat(seatMatrix)

    elif choice == "2":

        displayDashboard(seatMatrix)

    elif choice == "3":

        print("Exiting theater system...")
        break

    else:

        print("Invalid choice. Please try again.")