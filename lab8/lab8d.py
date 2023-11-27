# Write your code for lab 8d here.
from cal_abstraction import CalendarDay, Time
from cal_ui import *
from settings import CHECK_AGAINST_FACIT




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
    start_time = new_time_from_string(start)
    end_time = new_time_from_string(end)
    cal_year = get_calendar(cal_name)
    cal_month = cy_get_month(mon, cal_year)
    cal_day = cm_get_day(cal_month, day)
    create_free_time(cal_day, start, end)


#    basfall: om start appointment
#    iterera genom appointment list
#        skapa timespan av: slut tiden av i och start tiden av i+1
def create_free_time(cal_day: CalendarDay, start: Time, end:Time):
    for app in cd_iter_appointments(cal_day):
        start_app = ts_start(app_span(app))
        end_app = ts_end(app_span(app))
        #app 10:00 -12:00
        #free 08:00 - 13:00
            #10:00      #08:00       #

        if start_app <= start and end_app >= start:
            """This returns True if start   """
            free_time = new_time_span()
        elif start_app > start:
            
        #ts_end(app_span(app_1)) #ts_start(app_span(app_2))


def find_appointment(cal_day: CalendarDay, start: Time):
    """Searches through appointments to find the appointment that matches our start time"""
    for app in cd_iter_appointments(cal_day):
        if time_equals(start, ts_start(app_span(app))):
            return app

def free_spans(cal_day: CalendarDay, start: Time, end: Time) -> TimeSpanSeq:
    pass
