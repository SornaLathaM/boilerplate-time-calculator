def add_time(start, duration, day=None):
    weekdays = [
        'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
        'sunday'
    ]
    shour, am_pm = start.split()
    shour, smin = shour.split(':')
    dhour, dmin = duration.split(':')
    sum_hour = int(shour) + int(dhour)
    sum_min = int(smin) + int(dmin)
    if sum_min > 59:
        sum_hour += sum_min // 60
        min = sum_min % 60
    else:
        min = sum_min
    DaysLater = sum_hour // 24
    balhour = sum_hour % 24
    ampmcount = sum_hour // 12
    if balhour >= 12 and am_pm == 'AM':
        if balhour != 12:
            hour = balhour % 12
        else:
            hour = balhour
    elif balhour >= 12:
        DaysLater += 1
        if balhour != 12:
            hour = balhour % 12
        else:
            hour = balhour
    else:
        hour = balhour
    if ampmcount % 2 == 0:
        AMPM = am_pm
    else:
        if am_pm == 'AM':
            AMPM = 'PM'
        else:
            AMPM = 'AM'

    new_time = str(hour) + ':' + str(min).rjust(2, '0') + ' ' + AMPM
    if day:
        n = (weekdays.index(day.lower()) + DaysLater) % 7
        resday = weekdays[n]
        new_time += ', ' + resday.capitalize()

    if DaysLater == 1:
        new_time += ' (next day)'
    elif DaysLater > 1:
        new_time += ' (' + str(DaysLater) + ' days later)'
    return new_time
