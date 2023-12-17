import calendar


def main():
    # Get user input for day, month, and year
    day = int(input("Enter the day (1-31): "))
    month = int(input("Enter the month (1-12): "))
    year = int(input("Enter the year: "))

    # Validate input
    if not (1 <= day <= 31) or not (1 <= month <= 12):
        print("Invalid day or month. Please enter valid values.")
        return

    # Generate calendar for the specified month and year
    cal = calendar.monthcalendar(year, month)

    # Check if the user-provided day falls within the month
    if cal[0][0] == 0:
        # If the first day of the month is not in
        # # the first week, consider the second week
        week = cal[1]
    else:
        week = cal[0]

    # Check if the user-provided day is valid
    if week[day - 1] == 0:
        print("Invalid day for the specified month and year.")
        return

    # Print the calendar
    print("\nCalendar for {}/{}/{}:".format(day, month, year))
    print("\n".join([" ".join(map(str, week)) for week in cal]))


if __name__ == "__main__":
    main()
