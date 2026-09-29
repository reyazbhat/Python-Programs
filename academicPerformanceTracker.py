# Case Study 2: Student Academic Performance Tracker


# Task 1: Store student records in a dictionary
students = {
    101: ("Bob", "85", "78", "92"),
    102: ("Alica", "72", "81", "75"),
    103: ("Charlie", "91", "89", "95"),
   
}


# Task 2: Calculate average grade
def calculateAverage(math, science, english):

    math = float(math)
    science = float(science)
    english = float(english)

    average = (math + science + english) / 3

    return average

## Task 3: assign Grade

def assigngrade(average):

    if average >= 80:
        return "A"

    elif average >= 60:
        return "B"

    elif average >= 40:
        return "C"

    else:
        return "F"

##Task 4: Students according to the grade
def calculateRank(students):

    studentList = []

    for student_id, details in students.items():

        name = details[0]
        math = details[1]
        science = details[2]
        english = details[3]

        average = calculateAverage(math, science, english)

        grade = assigngrade(average)

        studentList.append(
            (student_id, name, average, grade)
        )

    studentList.sort(key=lambda student: student[2], reverse=True)

    return studentList


# Task 5: Student Gradebook Report
def displayReport(students):

    rankedStudents = calculateRank(students)

    print("=" * 75)
    print("                 STUDENT GRADEBOOK REPORT")
    print("=" * 75)

    print(
        f"{'Rank':<8}"
        f"{'ID':<8}"
        f"{'Name':<15}"
        f"{'Average':<12}"
        f"{'Grade':<8}"
        f"{'Status':<10}"
    )

    print("-" * 75)

    totalAverage = 0

    for rank, student in enumerate(rankedStudents, start=1):

        student_id = student[0]
        name = student[1]
        average = student[2]
        grade = student[3]

        if grade == "F":
            status = "Fail"
        else:
            status = "Pass"

        totalAverage += average

        print(
            f"{rank:<8}"
            f"{student_id:<8}"
            f"{name:<15}"
            f"{average:<12.2f}"
            f"{grade:<8}"
            f"{status:<10}"
        )

    classAverage = totalAverage / len(rankedStudents)

    print("-" * 75)
    print(f"Class Average: {classAverage:.2f}")
    print(f"Top Student: {rankedStudents[0][1]}")
    print(f"Top Average: {rankedStudents[0][2]:.2f}")
    print("=" * 75)


# Run the program
displayReport(students)