# ==================================================
# Case Study 8: Hospital Patient Priority Queue
# ==================================================


# ==================================================
# Task 1: Patient Waiting List
# ==================================================

patientQueue = []


# ==================================================
# Task 2: Add Patient
# ==================================================

def addPatient(patientQueue):

    patientName = input("Enter Patient Name: ")
    patientAge = int(input("Enter Patient Age: "))

    emergencyInput = input(
        "Is this an emergency? (yes/no): "
    ).lower()

    if emergencyInput == "yes":

        isEmergency = True

    else:

        isEmergency = False

    patient = {
        "name": patientName,
        "age": patientAge,
        "isEmergency": isEmergency
    }

    if isEmergency:

        patientQueue.insert(0, patient)

        print("Emergency patient added at the front of the queue.")

    else:

        patientQueue.append(patient)

        print("Regular patient added to the queue.")


# ==================================================
# Task 3: Call Next Patient
# ==================================================

def callPatient(patientQueue):

    if len(patientQueue) > 0:

        patient = patientQueue.pop(0)

        print("\nPatient called:")
        print("Name:", patient["name"])
        print("Age:", patient["age"])

    else:

        print("No patients are waiting.")


# ==================================================
# Task 4: Calculate Average Patient Age
# ==================================================

def calculateAverageAge(patientQueue):

    if len(patientQueue) == 0:

        return 0

    totalAge = 0

    for patient in patientQueue:

        totalAge += int(patient["age"])

    averageAge = float(totalAge) / len(patientQueue)

    return averageAge


# ==================================================
# Task 5: Hospital Dashboard
# ==================================================

def displayDashboard(patientQueue):

    averageAge = calculateAverageAge(patientQueue)

    print("\n")

    print("=" * 60)
    print("             HOSPITAL TRIAGE QUEUE DASHBOARD")
    print("=" * 60)

    print(
        f"{'Pos':<5}"
        f"{'Patient Name':<20}"
        f"{'Age':<6}"
        f"{'Priority Status':<15}"
    )

    print("-" * 60)

    for position, patient in enumerate(patientQueue, start=1):

        if patient["isEmergency"]:

            priorityStatus = "CRITICAL"

        else:

            priorityStatus = "REGULAR"

        print(
            f"{position:<5}"
            f"{patient['name']:<20}"
            f"{patient['age']:<6}"
            f"{priorityStatus:<15}"
        )

    print("-" * 60)

    print(
        f"Total Waiting Patients : {len(patientQueue)}"
    )

    print(
        f"Average Patient Age    : {averageAge:.1f} years"
    )

    print("=" * 60)


# ==================================================
# Interactive Menu
# ==================================================

while True:

    print("\n========== HOSPITAL MENU ==========")

    print("1. Add Patient")
    print("2. Call Next Patient")
    print("3. View Queue Dashboard")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        addPatient(patientQueue)

    elif choice == "2":

        callPatient(patientQueue)

    elif choice == "3":

        displayDashboard(patientQueue)

    elif choice == "4":

        print("Exiting hospital system...")
        break

    else:

        print("Invalid choice. Please try again.")