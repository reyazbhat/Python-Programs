# Case Study 3: Event Email Audit & VIP Entry


# Task 1: Raw registration data with duplicates

raw_registrations = [
    "alice@gmail.com",
    "bob@gmail.com",
    "charlie@gmail.com",
    "alice@gmail.com",
    "david@gmail.com",
    "bob@gmail.com",
    "emma@gmail.com",
    "frank@gmail.com"
]

# Convert list to set to remove duplicates
registered_users = set(raw_registrations)

# print(registered_users)

# VIP list
vip_list = {
    "alice@gmail.com",
    "david@gmail.com",
    "frank@gmail.com",
    "george@gmail.com"
}


# Actual attendees
attendees = {
    "alice@gmail.com",
    "charlie@gmail.com",
    "david@gmail.com",
    "emma@gmail.com"
}


# Task 2: Find VIPs who attended
vip_attendees = registered_users.intersection(vip_list)

print("VIP Attendees:")
print(vip_attendees)


# Task 3: Find registered people who did not attend
absentees = registered_users.difference(attendees)

print("\nAbsentees:")
print(absentees)


# Task 4: Check user registration
email = input("\nEnter your email: ")

email = email.lower().strip()

if email in registered_users:
    print("You are registered for the event.")

    if email in attendees:
        print("You have checked in successfully.")
    else:
        print("You are registered but did not check in.")

else:
    print("You are not registered for the event.")


# Task 5: Event Check-in Analytics Report

total_registered = len(registered_users)
total_attendees = len(attendees)
total_absentees = len(absentees)
total_vip_attendees = len(vip_attendees)

print("\n")
print("=" * 60)
print("           EVENT CHECK-IN ANALYTICS REPORT")
print("=" * 60)

print("Total Unique Registrants :", total_registered)
print("Total Attendees          :", total_attendees)
print("Total Absentees          :", total_absentees)
print("VIP Attendees            :", total_vip_attendees)

print("-" * 60)

attendance_percentage = (total_attendees / total_registered) * 100

print(f"Attendance Percentage    : {attendance_percentage:.2f}%")

print("=" * 60)