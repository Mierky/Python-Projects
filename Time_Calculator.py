def splitter_time(time):
    time2 = time.split(':')
    hours = time2[0].strip()
    minutes = time2[1].strip()
    return int(hours), int(minutes)


def test_days(hours, minutes, days, midday):
    if days == 0:
        new_time = f'{hours}:{minutes:02d} {midday}'
    elif days == 1:
        new_time = f'{hours}:{minutes:02d} {midday} (next day)'
    else:
        new_time = f'{hours}:{minutes:02d} {midday} ({days} days later)'
    return new_time


def add_time(start, duration, day=None):
    days_of_week = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    starting_time = start.split(' ')
    time = starting_time[0].strip()
    midday = starting_time[1].strip()

    hours_1, minutes_1 = splitter_time(time)
    hours_2, minutes_2 = splitter_time(duration)

    # Convert start time to 24-hour format
    if midday == 'PM' and hours_1 != 12:
        hours_1 += 12
    elif midday == 'AM' and hours_1 == 12:
        hours_1 = 0

    # Add the duration to the start time
    total_minutes = minutes_1 + minutes_2
    total_hours = hours_1 + hours_2 + (total_minutes // 60)
    total_minutes = total_minutes % 60
    days = total_hours // 24
    total_hours = total_hours % 24

    # Convert back to 12-hour format
    if total_hours == 0:
        final_hours = 12
        final_midday = 'AM'
    elif total_hours < 12:
        final_hours = total_hours
        final_midday = 'AM'
    elif total_hours == 12:
        final_hours = 12
        final_midday = 'PM'
    else:
        final_hours = total_hours - 12
        final_midday = 'PM'

    if day:
        day_index = days_of_week.index(day.capitalize())
        final_day_index = (day_index + days) % 7
        final_day = days_of_week[final_day_index]

        if days == 0:
            return f"{final_hours}:{total_minutes:02d} {final_midday}, {final_day}"
        elif days == 1:
            return f"{final_hours}:{total_minutes:02d} {final_midday}, {final_day} (next day)"
        else:
            return f"{final_hours}:{total_minutes:02d} {final_midday}, {final_day} ({days} days later)"
    else:
        return test_days(final_hours, total_minutes, days, final_midday)


print(add_time('3:00 PM', '3:10'))
print(add_time('11:30 AM', '2:32', 'Monday'))
print(add_time('10:10 PM', '3:30'))
print(add_time('11:43 PM', '24:20', 'tueSday'))