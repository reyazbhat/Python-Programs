# ==================================================
# Case Study 10: Fitness Tracker Activity Analytics
# ==================================================


# ==================================================
# Task 1: Store 7 Days of Activity Logs
# ==================================================

activityLogs = [

    {
        "day": "Mon",
        "steps": 10200,
        "calories": 450,
        "goalMet": True
    },

    {
        "day": "Tue",
        "steps": 8500,
        "calories": 380,
        "goalMet": True
    },

    {
        "day": "Wed",
        "steps": 4300,
        "calories": 200,
        "goalMet": False
    },

    {
        "day": "Thu",
        "steps": 11000,
        "calories": 500,
        "goalMet": True
    },

    {
        "day": "Fri",
        "steps": 9100,
        "calories": 410,
        "goalMet": True
    },

    {
        "day": "Sat",
        "steps": 7500,
        "calories": 350,
        "goalMet": False
    },

    {
        "day": "Sun",
        "steps": 8000,
        "calories": 360,
        "goalMet": False
    }
]


# ==================================================
# Task 2: Calculate Weekly Steps and Calories
# ==================================================

def calculateWeeklyStats(activityLogs):

    totalSteps = 0
    totalCalories = 0

    for activity in activityLogs:

        totalSteps += activity["steps"]

        totalCalories += activity["calories"]

    return totalSteps, totalCalories


# ==================================================
# Task 3: Count Days Goal Was Met
# ==================================================

def countGoalDays(activityLogs):

    goalDays = 0

    for activity in activityLogs:

        if activity["goalMet"] == True:

            goalDays += 1

    return goalDays


# ==================================================
# Task 4: Calculate Average Daily Steps
# ==================================================

def calculateAverageSteps(activityLogs):

    totalSteps, totalCalories = calculateWeeklyStats(activityLogs)

    averageSteps = totalSteps / len(activityLogs)

    averageSteps = int(averageSteps)

    return averageSteps


# ==================================================
# Task 5: Display Fitness Dashboard
# ==================================================

def displayDashboard(activityLogs):

    totalSteps, totalCalories = calculateWeeklyStats(
        activityLogs
    )

    goalDays = countGoalDays(activityLogs)

    averageSteps = calculateAverageSteps(activityLogs)

    goalCompletionRate = (
        goalDays / len(activityLogs)
    ) * 100

    print("\n")

    print("=" * 65)

    print("             WEEKLY FITNESS ANALYTICS REPORT")

    print("=" * 65)

    print(
        f"{'Day':<6}"
        f"{'Steps':<10}"
        f"{'Calories (kcal)':<20}"
        f"{'Daily Goal Met':<15}"
    )

    print("-" * 65)

    for activity in activityLogs:

        if activity["goalMet"] == True:

            goalStatus = "YES"

        else:

            goalStatus = "NO"

        print(
            f"{activity['day']:<6}"
            f"{activity['steps']:<10,}"
            f"{activity['calories']:<20}"
            f"{goalStatus:<15}"
        )

    print("-" * 65)

    print(
        f"Total Weekly Steps    : {totalSteps:,}"
    )

    print(
        f"Total Weekly Calories : {totalCalories:,} kcal"
    )

    print(
        f"Average Daily Steps   : {averageSteps:,}"
    )

    print(
        f"Goal Completion Rate  : {goalCompletionRate:.1f}%"
    )

    print("=" * 65)


# ==================================================
# Main Program
# ==================================================

displayDashboard(activityLogs)