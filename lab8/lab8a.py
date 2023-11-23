# This code violates abstraction layers, and should be reimplemented in lab 8A.
from cal_abstraction import *


def ts_equals(ts1: TimeSpan, ts2: TimeSpan): #KLAR
    """Return true iff the two given TimeSpans are equal."""
    ensure_type(ts1, TimeSpan)
    ensure_type(ts2, TimeSpan)
    
    return (time_equals(ts_start(ts1), ts_start(ts2)) and
            time_equals(ts_end(ts1), ts_end(ts2))) 


def ts_overlap(ts1: TimeSpan, ts2: TimeSpan) -> bool: #KLAR
    """Return true iff the two given TimeSpans overlap."""
    ensure_type(ts1, TimeSpan)
    ensure_type(ts2, TimeSpan)

    return (
            time_precedes(ts_start(ts1), ts_end(ts2)) and
                
            time_precedes(ts_start(ts2), ts_end(ts1))
    )


def ts_overlapping_part(ts1: TimeSpan, ts2: TimeSpan) -> TimeSpan: #KLAR
    """Return the overlapping part of two overlapping time spans,
    under the assumption that they really *are* overlapping."""
    ensure_type(ts1, TimeSpan)
    ensure_type(ts2, TimeSpan)
    ensure((ts1, ts2), lambda tup: ts_overlap(tup[0], tup[1]))

    start = time_latest(ts_start(ts1), ts_start(ts2)) 
    end = time_earliest(ts_end(ts1), ts_end(ts2)) 
    
    return new_time_span(start, end) 


def ts_duration(ts: TimeSpan) -> "Duration": #KLAR
    """Return the duration (length) of a TimeSpan"""
    ensure_type(ts, TimeSpan) 
    start = ts_start(ts) 
    end = ts_end(ts) 

    duration_first = (hour_number(time_hour(start)) * 60 + minute_number(time_minute(start)))

    duration_second = hour_number(time_hour(end)) * 60 + minute_number(time_minute(end)) 

    total_minutes = duration_second - duration_first
    duration_final = new_duration(new_hour(total_minutes // 60), new_minute(total_minutes % 60))

    return duration_final


def duration_is_longer_or_equal(d1: Duration, d2: Duration): #KLAR
    """
    Return true iff the first duration is longer than, or equally as long as,
    the second duration.
    """
    ensure_type(d1, Duration)
    ensure_type(d2, Duration)

    hours1 = duration_hour(d1)
    mins1 = duration_minute(d1)

    hours2 = duration_hour(d2)
    mins2 = duration_minute(d2)

    time1 = new_time(hours1, mins1)
    time2 = new_time(hours2, mins2)

    return time_precedes_or_equals(time2,time1)


def duration_equals(d1: Duration, d2: Duration): #KLAR
    """
    Return true iff the first duration is equally as long as,
    the second duration.
    """
    ensure_type(d1, Duration)
    ensure_type(d2, Duration)

    hour1 = hour_number(duration_hour(d1))
    hour2 = hour_number(duration_hour(d2))
    min1 = minute_number(duration_minute(d1))
    min2 = minute_number(duration_minute(d2))
    return (hour1, min1) == (hour2, min2)


if __name__ == "__main__":
    test_timespan_duration()
