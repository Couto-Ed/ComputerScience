def add_time(start, duration, day=None):
    # Maintaining Days in a week
    day_week = {
        "Saturday": 0,
        "Sunday": 1,
        "Monday": 2,
        "Tuesday": 3,
        "Wednesday": 4,
        "Thursday": 5,
        "Friday": 6
    }
    # Getting the data from start parameter
    time_start, midday = start.split()
    hour, minutes = time_start.split(':')
    hour = int(hour)
    minutes = int(minutes)

    # Getting data from duration parameter
    duration_hour, duration_minutes = duration.split(':')
    duration_hour = int(duration_hour)
    duration_minutes = int(duration_minutes)

    # Making the clock into 24 hour format for the calculations
    if midday == "PM":
        hour += 12

    # Calculating total hours, minutes
    total_minutes = minutes + duration_minutes
    final_minutes = total_minutes % 60
    extra_hours = total_minutes // 60
    total_hour = hour + duration_hour + extra_hours

    # final hours as per 12 Hour clock for final format
    trans_hour = (total_hour % 24) % 12

    # Edge case
    if trans_hour == 0:
        trans_hour = 12
    trans_hour = str(trans_hour)

    # total days 24 hr 1 day
    total_day = (total_hour // 24)

    # deciding mid day (AM/PM)
    calc_midday = ""
    if (total_hour % 24) <= 11:
        calc_midday = "AM"
    else:
        calc_midday = "PM"

    # Handling single digit minutes case
    if final_minutes <= 9:
        final_minutes = '0' + str(final_minutes)
    else:
        final_minutes = str(final_minutes)
    
    # final formation
    final_time = trans_hour + ":" + final_minutes + ' ' + calc_midday
    
    if day == None:
        if total_day == 0:
            return final_time
        if total_day == 1:
            return final_time + ' (next day)'
        return final_time + ' (' + str(total_day) + ' days later)'
    
    else:
        calc_day = (day_week[day.lower().capitalize()] + total_day) % 7
        for i, j in day_week.items():
            if j == calc_day:
                calc_day = i
                break
        
        if total_day == 0:
            return final_time + ', ' + calc_day
        
        if total_day == 1:
            return final_time + ', ' + calc_day + ' (next day)'
        
        return final_time + ', ' + calc_day + ' (' + str(total_day) + ' days later)'
