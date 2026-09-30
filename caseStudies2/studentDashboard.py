print("Student Result Dashborad")

name = input("Enter your name: ")
studentID = input("Enter your ID: ")


internalMarks = float(input("Enter the Internal marks Obtained outof 20: "))

if internalMarks > 20:
    print("Please enter correct marks")

assignmentMarks = float(input("Enter the Assignment Obtained outof 15: "))
if internalMarks > 15:
    print("Please enter correct marks")
midTermMarks = float(input("Enter the mid term marks Obtained outof 25: "))
if internalMarks > 25:
    print("Please enter correct marks")
endTermMarks = float(input("Enter the end term marks Obtained outof 50: "))
if internalMarks > 50:
    print("Please enter correct marks")

totalMarks = internalMarks + assignmentMarks + midTermMarks + endTermMarks
percentage = totalMarks / 100 * 100

print("\n--- Student Result ---")
print("Name:", name)
print("Student ID:", studentID)
print("Total Marks:", totalMarks)
print("Percentage:", percentage, "%")

if percentage >= 90:
    print("A++ Grade")
elif percentage >= 80:
    print("A Grade")
elif percentage >= 70:
    print("B++ Grade")
elif percentage >= 60:
    print("B Grade")
elif percentage >= 50:
    print("C++ Grade")
elif percentage >= 40:
    print("C Grade")
else:
    print("Fail")

if percentage >= 40:
    print("You are eligible")
else:
    print("You are not eligible")