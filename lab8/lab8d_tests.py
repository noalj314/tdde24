# Write your code for lab 8d here.

from test_driver import store_test_case, run_free_spans_tests


# Create additional test cases, and add to them to create_tests_for_free_span().

def create_tests_for_free_span() -> dict:
    """Create and return a number of test cases for the free_spans function"""
    test_cases = dict()
    # We test all extreme cases - such as: an appointment before interval start, an appointment after interval end, interval start and end time the same, interval with no bookings, entire interval booked.
    store_test_case(
        test_cases,
        1,
        start_str="08:00",  # Search interval starts
        end_str="21:00",  # Search interval ends
        booking_data=["07:00-09:00", "13:00-18:00"],  # This day's appointments
        exp_result=["09:00-13:00", "18:00-21:00"],
    )  # Expected free time
    store_test_case(
        test_cases,
        1,
        start_str="10:00",  # Search interval starts
        end_str="20:00",  # Search interval ends
        booking_data=["10:00-11:00", "19:00-21:00"],  # This day's appointments
        exp_result=["11:00-19:00"],
    )  # Expected free time
    store_test_case(
        test_cases,
        1,
        start_str="08:00",  # Search interval starts
        end_str="21:00",  # Search interval ends
        booking_data=[""],  # This day's appointments
        exp_result=["08:00--21:00"],
    )  # Expected free time
    store_test_case(
        test_cases,
        1,
        start_str="08:00",  # Search interval starts
        end_str="21:00",  # Search interval ends
        booking_data=["08:00-21:00"],  # This day's appointments
        exp_result=["No available time."],
    )  # Expected free time
    store_test_case(
        test_cases,
        1,
        start_str="08:00",  # Search interval starts
        end_str="21:00",  # Search interval ends
        booking_data=["07:00-09:00", "13:00-18:00"],  # This day's appointments
        exp_result=["09:00-13:00", "18:00-21:00"],
    )  # Expected free time
    store_test_case(
        test_cases,
        1,
        start_str="08:00",  # Search interval starts
        end_str="08:00",  # Search interval ends
        booking_data=["07:00-08:00", "08:00-09:00"],  # This day's appointments
        exp_result=[""],
    )  # Expected free time
    store_test_case(
        test_cases,
        1,
        start_str="00:00",  # Search interval starts
        end_str="07:00",  # Search interval ends
        booking_data=["03:00-04:00", "04:29-04:59", "07:00-07:00"],  # This day's appointments
        exp_result=["00:00-03:00", "04:00-04:29", "04:59-07:00"],
    )  # Expected free time

    # -------- YOUR TEST CASES GO HERE -----------------------
    # For each case, add a brief description of what you want to test.

    print("Test cases generated.")

    return test_cases


if __name__ == '__main__':
    # Actually run the tests, using the test driver functions
    tests = create_tests_for_free_span()
    run_free_spans_tests(tests)
