def add_time(start, duration, start_day=None):
    # Parse start time
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))

    # Parse duration time
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Calculate new time
    new_hour = start_hour + duration_hour
    new_minute = start_minute + duration_minute

    # Handle overflow of minutes
    new_hour += new_minute // 60
    new_minute %= 60

    # Handle overflow of hours
    days_later = new_hour // 12
    new_hour %= 12

    # Handle period (AM/PM)
    if period == "PM":
        days_later += new_hour // 12
        new_hour %= 12
        period = "AM" if days_later % 2 == 0 else "PM"

    # Format result time
    new_time = f"{new_hour:02d}:{new_minute:02d} {period}"

    # Format result day
    if start_day:
        start_day = start_day.capitalize()
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        start_index = days_of_week.index(start_day)
        new_index = (start_index + days_later) % 7
        new_day = days_of_week[new_index]
        new_time += f", {new_day}"

    # Format days later
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time

# Example usage:
result = add_time("3:00 PM", "3:10")
print(result)

result_with_day = add_time("11:30 AM", "2:32", "Monday")
print(result_with_day)
