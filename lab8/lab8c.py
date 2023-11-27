from cal_abstraction import *
from cal_ui import *
from lab8a import *
from lab8b import *

def print_remove():
    """Simple print function for removing appointments"""
    print("The appointment has been removed.")

def remove(cal_name: str, d: int, m: str, t: str) -> None:
    """Remove an appointment in the calendar with the given name """
    day = new_day(d)
    mon = new_month(m)
    start = new_time_from_string(t)
    cal_year = get_calendar(cal_name)
    cal_month = cy_get_month(mon, cal_year)
    cal_day = cm_get_day(cal_month, day)

    if not is_booked_from(cal_day, start):
        print("The proposed time is not booked.")
        return 

    if is_booked_from(cal_day, start): #remove if there is appointment
        new_year = minus_appointment(find_appointment(cal_day, start), cal_year, cal_month, cal_day)
        insert_calendar(cal_name, new_year)
        print_remove()


def find_appointment(cal_day: CalendarDay, start: Time):
    """Searches through appointments to find the appointment that matches our start time"""
    for app in cd_iter_appointments(cal_day):
        if time_equals(start, ts_start(app_span(app))):
            return app


def minus_appointment(app: Appointment, cal_year: CalendarYear, mon: Month, cal_day: Day):
    """Returns a new calendar that does not contain unwanted appointment"""
    old_cal_month = mon
    old_cal_day = cal_day

    new_cal_day = cd_minus_appointment(old_cal_day, app)
    new_cal_month = cm_plus_cd(old_cal_month, new_cal_day)
    new_cal_year = cy_plus_cm(cal_year, new_cal_month)

    return new_cal_year


def cd_minus_appointment(cal_day: CalendarDay, appointment: Appointment) -> CalendarDay:
    """
    Returns a copy of the given CalendarDay, where the given Appointment
    has been removed in its proper position.
    """
    ensure_type(appointment, Appointment)
    ensure_type(cal_day, CalendarDay)

    def remove_appointment(app: Appointment, appointments: List[Appointment]):
        """Removes an appointment from the appointments list"""
        new_appointments = appointments.copy()
        new_appointments.remove(app)
        return new_appointments

    return new_calendar_day(
        cd_day(cal_day), remove_appointment(appointment, cal_day.appointments))


# -- Tests
create("Jayne")
book("Jayne", 20, "sep", "15:00", "17:00", "Rob train")
book("Jayne", 20, "sep", "14:00", "14:30", "Rob train")

remove("Jayne", 20, "sep", "15:00")

show("Jayne", 20 ,"sep")


