from cal_abstraction import *

# =========================================================================
# Type definition
# =========================================================================

# Define the type somehow...  The initial "" is simply here as a placeholder.
TimeSpanSeq = ""

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


def tss_plus_span(tss, ts):
    pass


def tss_iter_spans(tss):
    pass


def show_time_spans(tss: TimeSpanSeq):
    """Prints out all timespans in a timespan sequence."""
    for ts in tss_iter_spans(tss):
        print(ts)


# Keep only time spans that satisfy pred.
# You do not need to modify this function.
def tss_keep_spans(tss, pred):
    result = new_time_span_seq()
    for span in tss_iter_spans(tss):
        if pred(span):
            result = tss_plus_span(result, span)

    return result

