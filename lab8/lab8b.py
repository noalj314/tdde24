from cal_abstraction import *

# =========================================================================
# Type definition
# =========================================================================

# Defines a new datatype
TimeSpanSeq = NamedTuple(
    "TimeSpanSeq", [('timespans', List[TimeSpan])]) # 10:00 - 12:00


# =========================================================================
#  Function implementations
# =========================================================================

def new_time_span_seq(timespans: List[TimeSpan] = None):
    """Creates a new timespan sequence."""
    if timespans is None: # skapar en tom TimeSpanSeq ifall det inte finns n
        timespans = []
    else:
        timespans = sorted(timespans, key=lambda ts: ts_start(ts))
    return TimeSpanSeq(timespans)


def tss_is_empty(tss: TimeSpanSeq):
    """Checks if given timespanseq is empty."""
    return not tss.timespans


def tss_plus_span(tss: TimeSpanSeq, ts: TimeSpan):
    """Adds a new time span to the input time span sequence."""
    ensure_type(ts, TimeSpan)
    ensure_type(tss, TimeSpanSeq)
    new_timespan = tss.timespans + [ts]
    return new_time_span_seq(new_timespan)


def tss_iter_spans(tss: TimeSpanSeq):
    """Iterates through the time spans within the given time span sequence."""
    ensure_type(tss, TimeSpanSeq)
    for ts in tss.timespans:
        yield ts


def show_time_spans(tss: TimeSpanSeq):
    """Prints out all timespans in a timespan sequence."""
    for ts in tss_iter_spans(tss):
        print(ts)


def tss_keep_spans(tss, pred):
    """Filters time spans from the input time span sequence based on the provided predicate."""
    result = new_time_span_seq()
    for span in tss_iter_spans(tss):
        if pred(span):
            result = tss_plus_span(result, span)

    return result

