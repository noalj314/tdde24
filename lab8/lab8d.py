    # Write your code for lab 8d here.
from cal_abstraction import CalendarDay, Time
from cal_ui import *
from settings import CHECK_AGAINST_FACIT
from lab8b import *



if CHECK_AGAINST_FACIT:
    try:
        from lab8a import TimeSpanSeq
    except:
        print("*" * 100)
        print("*" * 100)
        print("Kan inte hitta facit; ändra CHECK_AGAINST_FACIT i test_driver.py till False")
        print("*" * 100)
        print("*" * 100)
        raise
else:
    from lab8b import *


def show_free(cal_name: str, d: int, mon: str, start: str, end: str):
    day = new_day(d)
    mo = new_month(mon)
    start_time = new_time_from_string(start)
    end_time = new_time_from_string(end)
    cal_year = get_calendar(cal_name)
    cal_month = cy_get_month(mo, cal_year)
    cal_day = cm_get_day(cal_month, day)
    tss =free_spans(cal_day, start_time, end_time)
    for timespan in tss_iter_spans(tss):
        print(f"{new_str_from_time(ts_start(timespan))} - {new_str_from_time(ts_end(timespan))}")


def free_spans(cal_day: CalendarDay, start: Time, end: Time):
    """ Creates a list with all relevant (available) timespans in given calendar day. """
    free_time = []
    timespans = None
    timespans = appointments_within_timespan(cal_day, start, end)

    # In case there does not exist any appointments
    if not timespans:
        print(f"{new_str_from_time(start)} - {new_str_from_time(end)}")
        free_time.append(new_time_span(start,end))
        return new_time_span_seq(free_time)

    # Handle time before first appointment
    if time_precedes(start, ts_start(app_span(timespans[0]))):
        print(f"{new_str_from_time(start)} - {new_str_from_time(ts_start(app_span(timespans[0])))}")
        free_time.append(new_time_span(start,ts_start(app_span(timespans[0]))))

    # Loops through the appointments and appends all times between appointments to free_time
    for i in range(len(timespans) - 1):
        current_end = ts_end(app_span(timespans[i]))
        next_start = ts_start(app_span(timespans[i + 1]))

    # Handles all the appointments within the interval
        if time_precedes(current_end, end):
            free_time.append(new_time_span(current_end,next_start))
            print((f"{new_str_from_time(current_end)} - {new_str_from_time(next_start)}"))

    # Handle time after last appointment
    last_app_end = ts_end(app_span(timespans[-1]))
    if time_precedes(last_app_end, end):
        free_time.append(new_time_span(last_app_end, end))
        print(f"{new_str_from_time(last_app_end)} - {new_str_from_time(end)}")
    return new_time_span_seq(free_time)

def appointments_within_timespan(cal_day: CalendarDay, start: Time, end: Time):
    """ Searches through appointments to find the appointment that matches our timespan. """
    new_app_list = []
    new_time_span(start, end)
    for app in cd_iter_appointments(cal_day):
        if ts_overlap(app_span(app), new_time_span(start, end)):
            new_app_list.append(app)
    return new_app_list

def new_str_from_time(time: Time) -> str:
    """ Convert and return a Time object into a string in the 'HH:MM' format. """
    hour = hour_number(time_hour(time))
    minute = minute_number(time_minute(time))
    return f"{hour:02d}:{minute:02d}" #02d to make sure it is 2 digits


